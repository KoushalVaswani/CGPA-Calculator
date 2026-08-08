import streamlit as st
import plotly.express as px
import pandas as pd
from calculator import (
    calculate_cgpa,
    calculate_percentage,
    highest_sgpa,
    lowest_sgpa,
    average_sgpa
)
st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 CGPA Calculator")
st.caption("Calculate your CGPA, visualize semester performance, and track your academic progress.")

st.divider()
# Number of semesters
num_semesters = st.number_input(
    "Enter Number of Semesters",
    min_value=1,
    max_value=12,
    value=4,
    step=1
)

st.divider()

# Store all SGPA values
sgpas = []


# Dynamic Input Boxes
for i in range(num_semesters):

    col1, col2 = st.columns([4, 2])

    with col1:
        sgpa = st.number_input(
            f"Semester {i+1} SGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            step=0.01,
            format="%.2f",
            key=i
        )

    with col2:

        if sgpa >= 9:
            st.metric("Grade", "🌟 Excellent")

        elif sgpa >= 8:
            st.metric("Grade", "✅ Very Good")

        elif sgpa >= 7:
            st.metric("Grade", "👍 Good")

        else:
            st.metric("Grade", "⚠ Needs Work")

    st.progress(sgpa / 10)

    sgpas.append(sgpa)

if st.button("🎓 Calculate CGPA", use_container_width=True):

    cgpa = calculate_cgpa(sgpas)
    percentage = calculate_percentage(cgpa)
    highest = highest_sgpa(sgpas)
    lowest = lowest_sgpa(sgpas)


    st.success("✅ Calculation Completed Successfully!")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🎓 CGPA", f"{cgpa:.2f}")

    with col2:
        st.metric("📈 Percentage", f"{percentage:.2f}%")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("🏆 Highest SGPA", f"{highest:.2f}")

    with col4:
        st.metric("📉 Lowest SGPA", f"{lowest:.2f}")
    st.divider()

    st.subheader("📊 Performance Analytics")

    left, right = st.columns(2)

    st.divider()

    with left:

        st.markdown(
            "<h4>📈 Semester-wise Performance</h4>",
            unsafe_allow_html=True
        )

        df = pd.DataFrame({
            "Semester": [f"Sem {i+1}" for i in range(len(sgpas))],
            "SGPA": sgpas
        })

        fig = px.line(
            df,
            x="Semester",
            y="SGPA",
            markers=True,
            
        )

        fig.update_traces(
            line=dict(width=4),
            marker=dict(size=10)
        )

        fig.update_layout(
            template="plotly_dark",
            yaxis=dict(range=[0,10]),
            
        )

        st.plotly_chart(fig, use_container_width=True)
    with right:

        st.markdown(
            "<h4>🥧 Performance Distribution </h4>",
            unsafe_allow_html=True
        )

        performance = {
            "Excellent":0,
            "Very Good":0,
            "Good":0,
            "Needs Improvement":0
        }

        for sgpa in sgpas:

            if sgpa >= 9:
                performance["Excellent"] += 1

            elif sgpa >= 8:
                performance["Very Good"] += 1

            elif sgpa >= 7:
                performance["Good"] += 1

            else:
                performance["Needs Improvement"] += 1

        pie_df = pd.DataFrame({
            "Category": performance.keys(),
            "Semesters": performance.values()
        })

        fig2 = px.pie(
            pie_df,
            names="Category",
            values="Semesters",
            hole=0.45,
            
        )

        fig2.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )
        fig2.update_layout(showlegend=False)

        st.plotly_chart(fig2, use_container_width=True)
