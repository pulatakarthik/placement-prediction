import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "placement_model.pkl"

model = joblib.load(MODEL_PATH)
# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)
st.sidebar.title("📌 About This Project")

st.sidebar.markdown("""
### 🎓 Placement Prediction System

This application predicts a student's placement probability using a Machine Learning model.

### 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly

### 👨‍💻 Developed By

**Pulata Karthik**
""")

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>

.stApp{
    background:#0E1117;
}

h1,h2,h3,h4,h5,p,label{
    color:white;
}

.main-title{
    font-size:42px;
    font-weight:bold;
    color:white;
}

.sub-title{
    color:#9CA3AF;
    font-size:18px;
}

.card{

    background:#1A1D29;

    padding:25px;

    border-radius:18px;

    border:1px solid #2D3748;

    box-shadow:0px 8px 25px rgba(0,0,0,0.45);

}

div.stButton > button{

    width:100%;

    height:55px;

    font-size:20px;

    border-radius:12px;

    background:#3B82F6;

    color:white;

    border:none;

}

div.stButton > button:hover{

    background:#2563EB;

}
.metric-card{

    background:#111827;

    border-radius:18px;

    padding:20px;

    text-align:center;

    border:1px solid #2D3748;

    box-shadow:0 8px 20px rgba(0,0,0,.4);

}

.metric-icon{

    font-size:32px;

}

.metric-value{

    font-size:30px;

    font-weight:bold;

    color:#60A5FA;

}

.metric-title{

    color:#9CA3AF;

    font-size:15px;

}
.recommend-card{

    background:#111827;

    border-left:6px solid #3B82F6;

    padding:18px;

    border-radius:14px;

    margin-bottom:12px;

    color:white;

    font-size:17px;

    box-shadow:0px 5px 18px rgba(0,0,0,.35);

}
.summary-card{

    background:#111827;

    border-radius:16px;

    padding:20px;

    margin-top:15px;

    border:1px solid #2D3748;

    box-shadow:0px 6px 18px rgba(0,0,0,.35);

}

.summary-title{

    font-size:22px;

    font-weight:bold;

    color:white;

    margin-bottom:15px;

}

.summary-row{

    display:flex;

    justify-content:space-between;

    padding:8px 0;

    color:white;

    border-bottom:1px solid #2D3748;

}

.rating{

    text-align:center;

    font-size:28px;

    color:#FFD700;

    margin-top:15px;

}
</style>
""",unsafe_allow_html=True)

# -------------------- HEADER --------------------

st.markdown("<div class='main-title'>🎓 Placement Prediction System</div>",unsafe_allow_html=True)

st.markdown("<div class='sub-title'>AI Powered Career Prediction using Machine Learning</div>",unsafe_allow_html=True)

st.write("")

# -------------------- TWO COLUMNS --------------------

left,right = st.columns([1,2])

# ================= LEFT =================

with left:

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.subheader("👤 Student Information")

    cgpa = st.number_input(
        "CGPA",
        0.0,
        10.0,
        8.0,
        0.1
    )

    aptitude = st.number_input(
        "Aptitude Score",
        0,
        100,
        75
    )

    internship = st.selectbox(
        "Internship Experience",
        ["No","Yes"]
    )

    projects = st.slider(
        "Projects Completed",
        0,
        5,
        2
    )

    backlogs = st.slider(
        "Active Backlogs",
        0,
        3,
        0
    )

    st.write("")

    predict = st.button("🚀 Predict Placement")

    st.markdown("</div>",unsafe_allow_html=True)

# ================= RIGHT =================

with right:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Prediction Result")

    if predict:

        with st.spinner("🤖 AI is analyzing your profile..."):
            internship_value = 1 if internship == "Yes" else 0

        student = pd.DataFrame([{
            "CGPA": cgpa,
            "Aptitude_score": aptitude,
            "internship_experience": internship_value,
            "projects_completed": projects,
            "active_backlogs": backlogs
        }])

        # Prediction
        probability = float(model.predict(student)[0])

        probability = max(0, min(probability, 99))

        # ---------------- STATUS ----------------

        if probability >= 85:
            status = "Excellent"
            confidence = "Very High"

        elif probability >= 70:
            status = "High"
            confidence = "High"

        elif probability >= 50:
            status = "Moderate"
            confidence = "Medium"

        else:
            status = "Low"
            confidence = "Low"

        # ---------------- TOP CARDS ----------------

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">🎯</div>
                <div class="metric-value">{probability:.1f}%</div>
                <div class="metric-title">Placement Score</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-value">{status}</div>
                <div class="metric-title">Prediction Status</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">⭐</div>
                <div class="metric-value">{confidence}</div>
                <div class="metric-title">Confidence</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        if probability >= 70:
            gauge_color = "#22C55E"      # Green
        elif probability >= 50:
            gauge_color = "#F59E0B"      # Orange
        else:
            gauge_color = "#EF4444" 

        # ---------------- GAUGE ----------------

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability,

            number={
                "suffix": "%",
                "font": {"size": 42}
            },

            title={
                "text": "Placement Probability",
                "font": {"size": 22}
            },

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": gauge_color},

                "steps": [

                    {"range": [0, 40], "color": "#5B1F1F"},

                    {"range": [40, 70], "color": "#A67C00"},

                    {"range": [70, 100], "color": "#146C43"}

                ]

            }

        ))

        gauge.update_layout(

            height=330,

            margin=dict(l=10, r=10, t=40, b=10),

            paper_bgcolor="#1A1D29",

            font=dict(color="white")

        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )
        # ---------------- STUDENT SUMMARY ----------------

        if probability >= 85:
            stars = "★★★★★"
        elif probability >= 70:
            stars = "★★★★☆"
        elif probability >= 50:
            stars = "★★★☆☆"
        elif probability >= 30:
            stars = "★★☆☆☆"
        else:
            stars = "★☆☆☆☆"

        st.markdown(f"""
        <div class="summary-card">

        <div class="summary-title">
        👤 Student Summary
        </div>

        <div class="summary-row">
        <span>CGPA</span>
        <span>{cgpa}</span>
        </div>

        <div class="summary-row">
        <span>Aptitude Score</span>
        <span>{aptitude}</span>
        </div>

        <div class="summary-row">
        <span>Internship</span>
        <span>{internship}</span>
        </div>

        <div class="summary-row">
        <span>Projects</span>
        <span>{projects}</span>
        </div>

        <div class="summary-row">
        <span>Backlogs</span>
        <span>{backlogs}</span>
        </div>

        <div class="rating">
        {stars}
        </div>

        </div>
        """, unsafe_allow_html=True)
        # ---------------- FEATURE IMPACT ----------------

        st.subheader("📊 Feature Impact Analysis")

        impact = {
            "Feature": [
                "CGPA",
                "Aptitude",
                "Internship",
                "Projects",
                "Backlogs"
            ],
            "Impact": [
                cgpa * 3.5,
                aptitude * 0.3,
                internship_value * 15,
                projects * 4,
                -(backlogs * 8)
            ]
        }

        impact_df = pd.DataFrame(impact)

        fig = px.bar(
            impact_df,
            x="Impact",
            y="Feature",
            orientation="h",
            text="Impact",
            color="Impact",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            height=350,
            paper_bgcolor="#1A1D29",
            plot_bgcolor="#1A1D29",
            font_color="white",
            coloraxis_showscale=False,
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.divider()

        # ---------------- RECOMMENDATIONS ----------------

        st.subheader("💡 AI Recommendations")

        recommendations = []

        if aptitude < 85:
            recommendations.append("📘 Improve Aptitude Score to above **85**.")

        if internship == "No":
            recommendations.append("💼 Complete at least **one internship**.")

        if projects < 4:
            recommendations.append("🚀 Build **4+ real-world projects**.")

        if backlogs > 0:
            recommendations.append("📚 Clear all active backlogs.")

        if cgpa < 8:
            recommendations.append("🎓 Improve your CGPA to **8.0+**.")

        if len(recommendations) == 0:

            st.success("🎉 Excellent Profile! Keep maintaining your performance.")

        else:

            if aptitude < 85:
                st.info("📘 Improve your Aptitude Score to above 85.")

            if internship == "No":
                st.success("💼 Complete at least one Internship.")

            if projects < 4:
                st.warning("🚀 Build 4 or more Real-world Projects.")

            if backlogs > 0:
                st.error("📚 Clear all Active Backlogs.")

            if cgpa < 8:
                st.warning("🎓 Improve your CGPA to above 8.0.")

            if (
                aptitude >= 85 and
                internship == "Yes" and
                projects >= 4 and
                backlogs == 0 and
                cgpa >= 8
            ):
                st.success("🎉 Excellent Profile! Keep maintaining your performance.")

    else:

        st.info("👈 Enter your details and click **Predict Placement**.")

    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray;">

<h4>🎓 Placement Prediction System</h4>

<p>Developed by <b>Pulata Karthik</b></p>

<p>Python • Scikit-learn • Streamlit • Plotly</p>

<p>© 2026</p>

</div>
""",
unsafe_allow_html=True
)