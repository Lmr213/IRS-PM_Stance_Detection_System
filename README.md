SECTION 1 : PROJECT TITLE
Stance Detection System for combating Fake News


SECTION 2 : EXECUTIVE SUMMARY
In today’s information-driven society, the spread of misinformation, particularly fake news, has become a critical challenge that affects public trust, policy-making, and societal well-being. To address this issue, my project focuses on developing a Stance Detection System that automatically analyzes and classifies the relationship between a news headline and its corresponding body text. This system utilises advanced AI models, including SVM, XGBoost, LightGBM, CatBoost, and BERT, to provide highly accurate, real-time analysis aimed at identifying misleading or false information.

Through data preprocessing, feature engineering, and model training, we constructed a robust system capable of handling large datasets and complex text relationships. The system’s architecture integrates components for data input, preprocessing, feature extraction, model application, and result output, ensuring seamless performance from end to end. By automating stance detection, the system offers a scalable and efficient solution for media platforms, social media networks, and fact-checking organizations, reducing human error and minimizing the workload of manual verification processes.

In addition to addressing the technical aspects of AI model implementation, the project highlights the broader societal impact of combating misinformation. The use of traditional machine learning algorithms with deep learning models like BERT provides a balanced, scalable approach that is well-suited to real-world applications. This project serves as an example of how AI can be used to bridge the gap between academic research and practical tools, offering a significant contribution to the ongoing fight against fake news. Through this effort, I demonstrate how AI-driven solutions can enhance the reliability and efficiency of information verification processes in the digital age.

SECTION 3 : CREDITS / PROJECT CONTRIBUTION
Official Full Name	Student ID (MTech Applicable)	Work Items (Who Did What)	Email (Optional)
Lu Mingrui	A0307208L	All the tasks involved	E1391119@nus.edu.sg

SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO


SECTION 5 : USER GUIDE
Refer to file <Stance Detection System for combating Fake News - User Guide> in project report at Github Folder: Project Report & Appendices 

[ 1 ] To run the system using iss-vm
download pre-built virtual machine from http://bit.ly/iss-vm

start iss-vm

open terminal in iss-vm

$ git clone https://github.com/telescopeuser/Workshop-Project-Submission-Template.git

$ source activate iss-env-py2

(iss-env-py2) $ cd Workshop-Project-Submission-Template/SystemCode/clips

(iss-env-py2) $ python app.py

Go to URL using web browser http://0.0.0.0:5000 or http://127.0.0.1:5000

[ 2 ] To run the system in other/local machine:
Install additional necessary libraries. This application works in python 2 only.
$ sudo apt-get install python-clips clips build-essential libssl-dev libffi-dev python-dev python-pip

$ pip install pyclips flask flask-socketio eventlet simplejson pandas

SECTION 6 : PROJECT REPORT / PAPER
Refer to project report at Github Folder: ProjectReport

Recommended Sections for Project Report / Paper:

Executive Summary / Paper Abstract
Sponsor Company Introduction (if applicable)
Business Problem Background
Market Research
Project Objectives & Success Measurements
Project Solution (To detail domain modelling & system design.)
Project Implementation (To detail system development & testing approach.)
Project Performance & Validation (To prove project objectives are met.)
Project Conclusions: Findings & Recommendation
Appendix of report: Project Proposal
Appendix of report: Mapped System Functionalities against knowledge, techniques and skills of modular courses: MR, RS, CGS
Appendix of report: Installation and User Guide
Appendix of report: 1-2 pages individual project report per project member, including: Individual reflection of project journey: (1) personal contribution to group project (2) what learnt is most useful for you (3) how you can apply the knowledge and skills in other situations or your workplaces
Appendix of report: List of Abbreviations (if applicable)
Appendix of report: References (if applicable)
SECTION 7 : MISCELLANEOUS
Refer to Github Folder: Miscellaneous

HDB_BTO_SURVEY.xlsx
Results of survey
Insights derived, which were subsequently used in our system
