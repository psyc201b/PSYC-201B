# Syllabus

## When and where? 
**Communication**: [**Slack**](https://psyc201b.slack.com/) | [**Github**](https://github.com/psyc201b)  
**Location**: Mandler 3545 (Crick Conference Room)  
**Lectures**: Mon+Wed 2:00-3:50pm  
**Lab**: Tues 5:00-6:50pm  

<!-- ## About
As computers have become increasingly powerful modern statistical practice has changed, offering approaches that go far beyond standard methods taught in classic psychological statistics (Efron, Bradley, Hastie, Trevor {cite:year}`Efron2016`). And yet at the heart of these developments are just a handful of key ideas (Gelman, {cite:year}`Gelman2021`). This course is designed to help you interactively develop your own statistical intuitions about these ideas using the Python programming language. At the core of the class is a deep understanding of the General-Linear-Model (GLM) from which we’ll build-up additional concepts (e.g. linear-contrasts, mixed-effects-models) and connect to related ideas in machine-learning (e.g. resampling, cross-validation, regularization).  
**Requirements**: [PSYC 201A](https://canvas.ucsd.edu/courses/58741) or equivalent  
**Note**: this course will be taught in the *Python*, but experience in another language (e.g. R, Matlab) is sufficient

## Goals
- Build a strong foundation in statistics based on a deep understanding of the GLM
- Learn computational thinking, rather than statistical ritualizing - understanding the relationship between your analytic approach and what *inferences* are justified from first principles
- Develop *practical* Python programming, data analysis, and visualization skills
- Set you up for further coursework in advanced data-science, artificial intelligence, computational social science, or econometrics -->

## 2025 Instructional Team

```{list-table}
:header-rows: 1
* - 
  - [Eshin Jolly](https://eshinjolly.com)
  - [Khuyen Le](https://khuyen-le.github.io/)
  - [Ajinkya Jadhav](https://github.com/jajinkya211)
* - 
  - ![Eshin Jolly](/images/Eshin.jpg)
  - ![Khuyen Le](/images/Khuyen.jpg)
  - ![Ajinkya Jadhav](/images/Ajinkya.jpg)
* - Role
  - Instructor
  - Teaching Assistant
  - Teaching Assistant
* - Email
  - [e3jolly@ucsd.edu](mailto:e3jolly@ucsd.edu)
  - [khuyenle@ucsd.edu](mailto:khuyenle@ucsd.edu)
  - [asjadhav@ucsd.edu](mailto:asjadhav@ucsd.edu)
* - Slack
  - `@Eshin`
  - `@Khuyen Le`
  - `@Ajinkya`
* - Github
  - `@ejolly`
  - `@khuyen-le`
  - `@jajinkya211`
* - Office
  - Mandler 3509
  - McGill 2318
  - Mandler 1503
* - Office Hours
  - Wednesdays 4-5pm or by appt
  - Thursdays 9-10am
  - Tuesdays 1-2pm
```

## Class Format

### Github Classroom
We will be using **Github Classroom** to manage all lectures, labs, HWs, exams, and projects. Each week, we'll update the course website with links (prefixed with: 📚) to new Github Classroom assignments that contain all the materials you'll need for that day's lecture, labs, or HWs. **At the start of class/lab, or when a HW problem-set is made available, you should accept assignments and `git clone` them to your local computer to work interactively**.

When you're finished with an assignment or when you want to get feedback on work-in-progress, **you should `commit` your changes to your local copy of the assignment, and then `push` them to Github**. This will allow your instructors to review your work, provide Feedback, and/or have a private discussion with you while referencing questions/issues in your code directly. At the same time, you'll be building up a set of references (with feedback) that you can always check-out and refresh after this class is over!

We've made [instructions and a detailed tutorial video](/pages/github_classroom.md) about using Github Classroom available on the course website, under the *Computing Resources* section. If you *consistently* have trouble with Github Classroom, please reach out to your instructors for help and we can figure out solutions together.

### Course Website
When in doubt, the course website should be the first place you look for any logistical information! We'll be updating it regularly week-by-week with new **Course Topics** and **Course Labs**. You'll be able to *view* newly posted materials materials for each week on the website, but **you should be using the Github Classroom to submit your work to receive credit**. 

### Weekly Materials

You can find links to each week's materials by linking on that week from the left sidebar. Each week has an overview page with links to:

- Our plan for that week's topics (subject to change)
- 📚 links to Github Classroom assignments for that week's lecture & labs
- A notice at the top of the page with any HWs, links, and due dates
- Any required or suggested readings
- Additional helpful technical resources for that week's topics

### Communication

We will primarily be communicating using the course [Slack](https://psyc201b.slack.com/) so please make sure you join by the end of Week 1 or let your instructors know if you have any issues!

### Reading Materials

This website and linked materials will serve as the *primary digital textbook* for the course. **Required or optional readings/videos will be linked on that week's page**. We will be leaning heavily on readings from the following textbooks in addition to various assigned articles and will make PDFs available for any required readings:

1. [Statistical Thinking for the 21st Century](https://statsthinking21.github.io/statsthinking21-core-site/index.html) by Russ Poldrack
2. [Computational and Inferential Thinking: The Foundations of Data Science](https://inferentialthinking.com/chapters/intro.html) by Ani Adhikari, John DeNero, David Wagner.
3. [Elements of Statistical Learning](/pdfs/ESL.pdf) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman
4. [Regression and other stories](/pdfs/ROS.pdf) by Andrew Gelman, Jennifer Hill, and Aki Vehtari
5. [The Truth about Linear Regression](/pdfs/TALR.pdf) by Cosma Rohilla Shalizi
6. [Statistical Methods for Behavioral and Social Sciences](https://psych252.github.io/psych252book/) by Tobias Gestenberg

### Computing Resources
During Week 1, your instructors will help you configure your own computer so you have a working version of Python, scientific libraries we'll use, git/github configured to fetch and submit assignments, and code-editor (JupyterLab or VSCode) setup so you can work on notebook files interactively. If you have consistent issues with your local computer, please reach out to your instructors and we can help setup a [UCSD provided Jupyterhub instance](https://datahub.ucsd.edu/hub/login?next=%2Fhub%2F) or a [Github CodeSpace](https://github.com/features/codespaces) for you to work from.

Throughout the term, we'll link to additional resources and guides under the *Computing Resources* section of the course website. These include a variety of introductory tutorials, [cheatsheets](/pages/cheatsheets), and with a [glossary of terminology](/pages/glossary) to help you navigate the scientific Python ecosystem.

## Course work and grading

Course work and grading will primarily consist of:

- interactive lectures
- interactive labs
- weekly HW problem-sets
- a take-home midterm and final project 

### Lectures
During lectures, we will step-through interactive [Python notebooks](https://jupyter.org/) together explaining core statistical concepts with a combination of illustrative examples, widgets, mini-exercises, and larger challenges. Where needed, we'll refer to additional slides and materials. Because of varied experience levels, it's likely we won't always be able to complete the full set of notebooks when we meet. When this happens, **we expect you to walk through and attempt anything we don't finish yourself outside of scheduled class time and push your changes to Github**. Your instructors will be available to answers questions over Slack, Github, or in-person. Unless otherwise noted, you don't need to look at materials ahead of lecture, but should **prepared to participate in any class discussions**.

### Labs
During labs, we'll build upon ideas introduced in lectures, deep-dive into scientific Python libraries and their particulars, and review HW problem-sets as needed. Previous Python experience is *not required*, but prior programming experience in another language (e.g. R, Matlab) is helpful. We'll start slow and provide plenty of resources, links, and additional tutorials on the course website. Labs will also familiarize you with any additional tools you'll be using to complete and submit assignments (i.e. jupyter notebooks, github classroom, etc). At the end of each lab, you'll be asked to **submit your work to Github Classroom**, and your instructors will be available to answer questions over Slack, Github, or in-person.

### Homework Problem-sets
Approximately every week, you'll receive a problem-set of questions covering that week's topics. Unless otherwise noted, problem-sets will always be due the **Sunday before class at midnight PST**. You should complete and submit problems using Github Classroom, submitting any code, figures, and prose that answer the questions. **You are encouraged to work on weekly assignments with other students**. However, you should list the names of all students you worked with in the notebook you submit.

### Midterm & Final
The midterm will be a take-home exam that will consist of questions similar to the weekly problem-sets, **however you must complete the midterm by yourself**.  

For the final, depending on our progress throughout the term, your instructors and I will give you the choice of several options:
- a novel analysis of your own/your lab's data 
- a novel analysis of a publicly available open dataset
- paired problem-set generation, where you and another student will generate and score problem sets for each other
- challenge questions generated by your instructors similar to weekly problem-sets and the midterm

More details about the final will be provided later in the term on the course website.

### Grading

**Mastery based grading.** We’re interested in grading you on your ability to achieve the skill sets that are taught in this course. Except for the mid-term and final, **you're allow to resubmit any Github Classroom Assignment more than once, if you feel like you could do better, or if you want to incorporate instructor feedback**. We'll grade you based *partially* on your accurate completion of the assignment, but *mostly* on your ability to demonstrate:

- You attempted the assignment in good-faith (lecture, lab, or HW notebooks)
- You made effort to clearly document and explain your thought process, reasoning, code, and where/why you got stuck if you did
- What attempts you made to fix issues you ran into, how you approached debugging, and what you learned from the process
- Why you made a particular choice in your code/analysis, and/or what assumptions you made for a particular statistical inference

**Cooperative extra-credit.** When working with other students on problem-sets, you have the opportunity to earn extra-credit. Working collaboratively with others is not sufficient for extra-credit. You can only submit a consideration for extra-credit if you and/or your peers feel like you went *above-and-beyond* on a given weekly problem-set. To do so, include a note in your jupyter notebook, indicating either: (a) who you helped, how, and what they learned; OR (b) who helped you, how, and what you learned. Extra credit can contribute up to 10% of your final grade.

**Grading Breakdown**: Your final course grade will be calculated based on:  

1. **Class participation (30%)**
    - attending lectures and labs
    - submitting lecture and lab notebooks to Github Classroom
    - asking & answering questions (code-review) about submitted assignments using the Feedback Pull-Request on your assignment repository
    - completing any required readings and participating in class discussions
2. **Weekly problem-sets (20%)**
    - ~8 total, ~2-3% each
    - attempting and submitting weekly problem-sets to Github Classroom, alone or with peers
    - working with other students to help each other out (and possibly extra-credit)
    - demonstrating improvement by updating your submissions based on instructor feedback
3. **Midterm problem-set (20%)**
    - attempting and submitting the midterm problem-set to Github Classroom, alone
4. **Final project (30%)**
    - TBD choose your option

## Academic Integrity
All students are expected to adhere to standards of academic integrity. Cheating of any kind on any assignment will not be tolerated. It is disrespectful to your peers, the university, and to your instructors. If you are unsure what might constitute a violation of academic integrity, ask your instructors and/or the UCSD website on academic integrity: [http://academicintegrity.ucsd.edu](http://academicintegrity.ucsd.edu.). Any evidence of academic misconduct will be reported to the Academic Integrity Office.

### Generative AI Course Policy
*Adapted from the UC San Diego & University of Waterloo Academic Integrity Offices*  

```{warning}
*GenAI is known to fabricate sources, facts, and give false information. It also perpetuates bias. You should also be aware that there are copyright and privacy concerns with these tools. You should exercise caution when using large portions of content from AI sources for these reasons. Also, you are accountable for the content and accuracy of all work you submit in this class, including any supported by generative AI.* 
```

We encourage the use of Generative artificial intelligence (GenAI) tools like [OpenAI's ChatGPT](https://chatgpt.com/), [Anthropic's Claude](https://claude.ai/), [Github's Co-pilot](https://github.com/features/copilot), or [Google's Gemini](https://gemini.google.com/app) to help you master concepts and skills in this class in accordance with the [UCSD Academic Integrity Guidelines on GenAI](https://academicintegrity.ucsd.edu/excel-integrity/gen-ai/ai-in-education.html) and the following guidelines:

1. If you use GenAI for any submitted coursework, you **must attach a link or text transcript** to any assignments you submit. Many services offer a "share your chat" link-creation function or you can use a Google Chrome Browser Extension like [ChatGPT Exporter](https://chromewebstore.google.com/detail/chatgpt-exporter-extract/ilmdofdhpnhffldihboadndccenlnfll?hl=en) or [Claude Exporter](https://chromewebstore.google.com/detail/claude-exporter-extract-c/elhmfakncmnghlnabnolalcjkdpfjnin). This will help us provide feedback on using LLM tools effectively (if desired) and make it transparent to us how you are completing assignments, while respecting the standards of academic integrity.
2. Directly prompting GenAI with course assignments, or copying/pasting GenAI output instead of performing the work yourself, **will not earn you assignment credit** and **could result in an academic integrity violation**. 

Instead you should aim to **master GenAI as tools** that supplement your programming and critical thinking skills, not as a substitute for them. They can be especially helpful for: debugging and troubleshooting unfamiliar code, reviewing Python fundamentals, reasoning about statistical concepts via analogy/example, or simply conversing in natural language about technical concepts. 

### Absence policy
Family emergencies and illness are excused absences, as per UCSD policy. Please do not come to class if you have active symptoms (instead, please rest!). In general, absences will have a direct impact on your ability to learn the skills presented in this course as well as your participation grade. 

**Life happens**. That being said, I really care about you, and your well-being. I know that life happens, and that sometimes you simply can’t be in class or turn in an assignment on time. There may also be times when I am unable to make it to class for a given reason, and I will ask for your grace and understanding then as well.  Please, prioritize your well-being in graduate school and use this class as a way for you to learn skills that will be useful for your career (versus focusing on passing the requirements for a grade). 

### OSD Accommodations
Any student with a documented disability will be accommodated according to University policy. For details, please consult the Office of Students with Disabilities (OSD): [http://disabilities.ucsd.edu](http://disabilities.ucsd.edu). If you require accommodation for any component of the course, please provide the instructor with documentation from OSD as soon as possible. Please note that accommodations cannot be made retroactively under any circumstances. 
