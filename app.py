from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "IMG0266.JPG"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Billiam Stewart Rodriguez"
PAGE_ICON = ":random:"
NAME = "Billiam Stewart Rodriguez"
DESCRIPTION = """
Highly experienced Port Operation Director with 22 years in the U.S Navy, specializing in strategic planning, financial management, and operational optimization. Skilled in data analysis using Tableau and Excel to improve efficiency and reduce costs. Holds an active **Security Clearance** with a successful track record in managing operations and leading cross-functional teams.
"""
EMAIL = "billstewrod@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/billiamstewartrodriguez",
    "Facebook": "https://facebook.com/djcalanco",
    "Instagram": "https://instagram.com/djcalanco",
}
PROJECTS = {
    "GitHub": "https://github.com/BillStewRod",
    "DataWars": "https://profiles.datawars.io/djcalanco",
    "FreeCodeAcademy": "https://www.freecodecamp.org/BillyTheGreat",
    "Microsoft Learning": "https://learn.microsoft.com/en-us/users/billiamstewartrodriguez-8322",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- 10 Years expereince extracting actionable insights from data
- Strong hands on experience and knowledge in Python and Excel
- Good understanding of statistical principles and their respective applications
- Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- Programming: Python (Pandas, NumPy, jQuery, VisiData), C#, C/C++, R, SQL, PERL, VB
- Data Visulization: PowerBi, MS Excel, Tableau
- Operating Systems: Windows, MacOS, Linux
- Databases: MariaDB, CrateDB, MySQL
- Software: MS Office Suite, Visual Studio/Code, GitHub Desktop, Anaconda
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Professional Experience")
st.write("---")

# --- JOB 1
st.write("**Port Operations Director  | UNITED STATES NAVY**")
st.write("Sep 2022  - Present")
st.write(
    """
- • Designed financial dashboard in Tableau to assess budgetary performance and identify potential variances for a $100k annual budget. Spearheaded initiative-taking resource allocation strategies for optimization
- •	Analyzed financial data to develop cost-effective strategies aligned with cost accounting principles. Achieved significant budget savings and streamlined operations, increasing efficiency by 25% in the first year.
- •	Condensed complex financial data into executive-level briefs, highlighting KPIs and potential risks. Facilitated quantitative support for the Command Triad with clear and effective communication.
"""
)

# --- JOB 2
st.write('\n')
st.write("**Surface Operations Director  | UNITED STATES NAVY**")
st.write("Aug 2021 - Aug 2022")
st.write(
    """
- • Executed objective judgment to enhance Naval Security Force initiatives, port operations, and emergency preparedness. Optimized resource allocation through rigorous analysis of multiple base exercises.
- •	Spearheaded a comprehensive transformation of the Selection and Application Process with Navy Personnel Command, significantly improving Naval Security forces' efficiency, expanding civilian roles, and reducing overtime costs by over 50k in the first year.
- •	Review and ensure compliance with Risk Management Framework (RMF) documentation, including Certification and Accreditation (C&A) Plan, Implementation Plan, Test Plan, quarterly System Plan of Actions and Milestones (POA&M), and Validation Report.
"""
)

# --- JOB 3
st.write('\n')
st.write("**Aircraft Division Director | UNITED STATES NAVY**")
st.write("Mar 2018 - Aug 2021")
st.write(
    """
- •	Enhanced data integrity and analytics efficiency within aircraft engine repair processes. Consolidated disparate worksheets and leveraged PivotTables for streamlined analysis, contributing to a 28% reduced repair costs and optimized asset management.
- •	Performed in-depth inventory trend analysis using ad-hoc queries, ensuring the availability of 52 aircraft engines during deployment. Innovative resource allocation minimized operational disruptions.
- •	Developed performance metrics to assess the Aircraft Division's effectiveness. Identified skill gaps and implemented targeted training initiatives, directly boosting workforce productivity.
- •	Collaborated with Maintenance Officers to strategically identify engine trends, informing strategic maintenance planning. Resulted in a 98% increase in aircraft availability, minimizing operational disruptions.
"""
)

# --- JOB 4
st.write('\n')
st.write("**Navy Oil Analysis Program Manager | UNITED STATES NAVY**")
st.write("Mar 2018 - Aug 2020")
st.write(
    """
- •	Developed a spectrometric oil analysis program and data tracking system in Excel to safeguard equipment investment via descriptive statistics. Anticipatory maintenance strategies significantly reduced the financial risk of unexpected breakdowns.
- •	Analyzed engine component failure rates using survival analysis and Excel to establish a predictive maintenance strategy. Optimized budgeting for replacement parts and streamlined analysis process optimization.
- •	Provided evidence-based maintenance feedback with time series analysis, reducing unscheduled downtime by 20%. Improved operational efficiency and maximized asset availability for mission-critical operations.
"""
)

# --- JOB 5
st.write('\n')
st.write("**Gas Turbine Engine Test Facility (ETF) Program Manager | UNITED STATES NAVY**")
st.write("Mar 2018 - Mar 2020")
st.write(
    """
- •	Successfully operated and maintained Jet Engine Test Instrumentation (JETI) system, consisting of two interconnected Windows servers via Ethernet. 
- •	Oversaw comprehensive monitoring and display of engine parameters during testing, integrating six critical functions: instrumentation, data acquisition, system processor-controller, programmable throttle system, distributed electrical power, and operator-maintenance control and display. 
- •	Achieved 100% engine availability during a 10-month deployment, testing 46 F414 engines. 
- •	Analyzed training needs, designed analytics-driven training strategy using Excel PivotTables, and optimized budget allocation, resulting in rapid qualification of eight personnel for pre-deployment requirements.
"""
)

# --- JOB 6
st.write('\n')
st.write("**Command Financial Specialist Program Manager | UNITED STATES NAVY**")
st.write("Sep 2018 - Sep 2019")
st.write(
    """
- •	Served as a financial advisor for a large military command providing guidance on budgeting, debt management, and investment strategies. Significantly increased participation in retirement savings plans by 27%, promoting financial well-being.
- •	Analyzed financial data to develop comprehensive reports, highlighting trends and insights to facilitate information-centric decision-making. Enhanced financial literacy across the organization by delivering 24 workshops.
- •	Provided personalized financial counseling to 2,800 personnel through 294 sessions. Empowered individuals to make informed financial decisions, supporting fiscal responsibility and long-term financial health.
"""
)

# --- JOB 7
st.write('\n')
st.write("**Advanced Skills Aviation Mechanic Course Director | UNITED STATES NAVY**")
st.write("Jul 2015 - Feb 2018")
st.write(
    """
- •	Managed $75M in critical training assets, including aircraft engines, ensuring continuous availability for interactive instruction. Streamlined technical support processes, boosting training efficiency by 22% and maximizing the impact of training investments.
- •	Managed a large-scale training operation for 31 instructors and 1,680 students across four courses. Optimized resource allocation, significantly reducing class wait times to 10 days and achieving a 99% graduation rate.
- •	Leveraged Microsoft Applications and Authoring Instructional Materials (AIM) Software to analyze training data. Informed curriculum updates and optimized course delivery across 100+ modules, enhancing training outcomes through objective decisions. 
"""
)

# --- JOB 8
st.write('\n')
st.write("**Maintenance Manager | UNITED STATES NAVY**")
st.write("Nov 2014 - Jun 2015")
st.write(
    """
- •	Led maintenance control for 14 work centers across multiple countries, streamlining operations to prioritize workloads. Optimized asset availability by 48%, ensuring readiness for critical missions.
- •	Collaborated with work center supervisors, leveraging DoD Financial Systems (Federal Mall, Naval Supply Systems Command OneTouch) to identify workload restrictions and potential issues. Improved production output by 34% and reduced "Beyond Capability of Maintenance" submissions by 50%.
- •	Reactively analyzed maintenance data using Decision Knowledge Programming (DECKPLATE) and Optimized Organizational Maintenance Activity System (OOMA) databases to identify aircraft engine maintenance trends for 13 P-3C aircraft. Generated reports in Excel, supporting metrics-based decision optimization to enhance aircraft availability.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
cols = st.columns(len(PROJECTS))
for index, (platform, link) in enumerate(PROJECTS.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Soft Skills SECTION ---
st.write('\n')
st.subheader("Soft Skills")
st.write("---")
col1, col2, col3, col4 = st.columns(4, gap="small")
with col1:
    st.write("• Problem-Solving") 
    st.write("• Decision-Making") 
    st.write("• Critical Thinking")

with col2:
    st.write("•	Willingness to Learn") 
    st.write("• Openness to Change") 
    st.write("• Leadership")

with col3:
    st.write("• Active Listening") 
    st.write("• Flexibility") 
    st.write("•	Networking")

with col4:
    st.write("•	Time Management") 
    st.write("•	Organizational Skills") 
    st.write("•	Verbal/Written Communication")
