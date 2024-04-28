## Resume Reviewer Project

### Project Overview
The Resume Reviewer is a powerful tool designed to assist users in refining their resumes. 
By utilizing GPT-based technology, the project offers personalized feedback on the content of resumes, focusing on the effectiveness and impact of the wording and sentence structures. 
Users can upload their resume in PDF format, and the system will provide constructive feedback to enhance their presentation and improve their chances in the job market.

### Getting Started

#### Prerequisites
- Ensure you have Python installed on your machine. You can download it from [Python's official site](https://www.python.org/downloads/).

#### Installation and Setup
1. **Clone the repository**
   git clone [repository-url]
   cd [repository-directory]

2. **Set up the API key**
   - Obtain your GPT API key from the provider.
   - Create a file named `.env` in the project root directory.
   - Add the following line to the `.env` file:
     OPENAI_API_KEY='your_api_key_here'


3. **Create a virtual environment**
   - python -m venv venv
  

4. **Activate the virtual environment**
   - For Windows:
     .\venv\Scripts\activate
   - For Unix or MacOS:
     source venv/bin/activate
     

5. **Install required packages**
   pip install -r requirements.txt
   - If any required tools are not installed, you may need to install them manually.

6. **Start the Flask application**
   flask run

### Usage
Once the application is running, navigate to `http://127.0.0.1:5000/` on your web browser.
Upload your PDF resume using the interface provided, and submit it to receive feedback.
The system will analyze your resume and return detailed feedback on how to improve your resume sentences and wording.

### Link to Demo: 
https://youtu.be/Evn-plJZiqs

