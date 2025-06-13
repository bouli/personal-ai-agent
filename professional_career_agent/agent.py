from google.adk.agents import Agent

def get_contact_info():
    """
    Retrieves contact information for Cesar Cardoso.
    """
    return {
        "email": "Please ask the email by Linkedin",
        "phone": "Please ask the phone by Linkedin",
        "github": "https://github.com/bouli",
        "linkedin": "https://www.linkedin.com/in/cesardesouzacardoso/", # Adicionei o LinkedIn com base no "Links" da página 3
        "address": "Hamburg - Germany"
    }

def get_professional_experience():
    """
    Retrieves professional experience for Cesar Cardoso.
    """
    experience = [
        {
            "company": "Laboratoria",
            "type": "NGO - Education/Gender Equality",
            "roles": [
                {
                    "title": "Lead Data Engineer",
                    "dates": "Jul 2021 - Jun 2024",
                    "responsibilities": "Responsible for Data Strategy, designing and implementing ETL, pipeline orchestration, data quality, data integrity and data monitoring using GCP (Functions, BigQuery, Storage), SQL and Python (PySpark, Pandas, NumPy).",
                    "location": "Lima - Perú (remote)"
                },
                {
                    "title": "Lead Software Engineer",
                    "dates": "Oct 2018 - Jul 2021",
                    "responsibilities": "Responsible for designing, building and maintaining softwares with product owners and developer team using NodeJS, React, MongoDB and Firebase as stack.",
                    "location": "Lima - Perú (remote)"
                }
            ]
        },
        {
            "company": "TECHO International",
            "type": "NGO - Poverty Fighting",
            "roles": [
                {
                    "title": "IT Director",
                    "dates": "Jun 2016 - Oct 2018",
                    "responsibilities": "Responsible for Technology Strategy, systems implementation and management with 21 countries of Latin America, Caribe and USA.",
                    "location": "Santiago - Chile"
                }
            ]
        },
        {
            "company": "Alfaiataria Digital",
            "type": "Advertisement",
            "roles": [
                {
                    "title": "Project Manager",
                    "dates": "Oct 2014 - May 2016",
                    "responsibilities": "Responsible for multiple tech development squads working with website development and online advertisement.",
                    "location": "São Paulo | SP - Brazil"
                },
                {
                    "title": "PHP Developer",
                    "dates": "Feb 2012 - Aug 2012",
                    "responsibilities": "System development using PHP, MySql, WordPress and FaceBook integration.",
                    "location": "São Paulo | SP - Brazil"
                }
            ]
        },
        {
            "company": "ERPFlex",
            "type": "ERP Systems",
            "roles": [
                {
                    "title": "Flex PHP Developer",
                    "dates": "Aug 2012 - Sep 2014",
                    "responsibilities": "ERP System development using PHP, Adobe Flex, MySql.",
                    "location": "São Paulo | SP - Brazil"
                },
                {
                    "title": "Flex PHP Developer",
                    "dates": "Jan 2010 - Jul 2011",
                    "responsibilities": "ERP System development using PHP, Adobe Flex, MySql.",
                    "location": "São Paulo | SP - Brazil"
                }
            ]
        },
        {
            "company": "RAPP Brasil",
            "type": "Advertisement",
            "roles": [
                {
                    "title": "PHP Developer",
                    "dates": "Aug 2011 - Oct 2011",
                    "responsibilities": "System development using PHP, MySql, WordPress and FaceBook integration.",
                    "location": "São Paulo | SP - Brazil"
                }
            ]
        },
        {
            "company": "Agência Incandescente",
            "type": "Digital Marketing",
            "roles": [
                {
                    "title": "IT Director (Co-Founder)",
                    "dates": "Jul 2009 - Feb 2012",
                    "responsibilities": "Responsible for technology strategy, product design and development.",
                    "location": "São Paulo | SP - Brazil"
                }
            ]
        },
        {
            "company": "Click; Pronto",
            "type": "Software Factory",
            "roles": [
                {
                    "title": "PHP Developer",
                    "dates": "May 2008 - Dec 2009",
                    "responsibilities": "ERP System development using PHP, ASP.NET, CSS, Javascript, Flash, Ajax, MySql, SQL Server.",
                    "location": "Santo André | SP - Brazil"
                }
            ]
        },
        {
            "company": "OiC - Optical Imaging Comercial",
            "type": "Websites",
            "roles": [
                {
                    "title": "PHP Developer Intern",
                    "dates": "Jan 2008 - May 2008",
                    "responsibilities": "System development using ASP.NET, PHP, CSS, Javascript, Adobe Flash, Ajax, Oracle.",
                    "location": "São Bernardo do Campo | SP - Brazil"
                }
            ]
        }
    ]
    return experience

def get_education_info():
    """
    Retrieves educational information for Cesar Cardoso.
    """
    education = [
        {
            "degree": "Postgraduate Studies Human Sciences",
            "major": "Sociology, History and Philosophy",
            "dates": "Aug 2020 - Dec 2021",
            "institution": "PUC Pontifícia Universidade Católica do Rio Grande do Sul",
            "location": "Porto Alegre | RS | Brazil"
        },
        {
            "degree": "Bachelor's Degree",
            "major": "System Analysis and Development",
            "dates": "Jul 2005 - Jun 2008",
            "institution": "Faculdade Engenheiro Salvador Arena",
            "location": "São Bernardo do Campo | SP | Brazil"
        },
        {
            "degree": "High School",
            "major": "System Analysis and Development Information Technology",
            "dates": "Jul 2004 - Dec 2005",
            "institution": "ETEC Lauro Gomes",
            "location": "Mauá | SP | Brazil"
        }
    ]
    return education

def get_sabbatical_experience():
    """
    Retrieves sabbatical experience for Cesar Cardoso.
    """
    sabbatical = [
        {
            "course": "German Language Course",
            "dates": "Feb-Mar 2025",
            "description": "German course in Germany.",
            "institution": "Goethe-Institute Hamburg, Germany"
        },
        {
            "course": "Japanese Language & Culture Course",
            "dates": "Oct 2024",
            "description": "Japanese and Japan Culture course in Japan.",
            "institution": "Akita Inaka School - Kosaka, Japan"
        },
        {
            "course": "Audio Engineering Fundamentals and Digital Mixers",
            "dates": "Jul-Aug 2024",
            "description": "Audio Engineering courses at IAV",
            "institution": "Instituto de Áudio e Vídeo - São Paulo, Brazil"
        }
    ]
    return sabbatical

def get_languages():
    """
    Retrieves language skills for Cesar Cardoso.
    """
    languages = [
        {"language": "Brazilian Portuguese", "proficiency": "Native", "level": "C2"},
        {"language": "Spanish", "proficiency": "Fluent", "level": "C1"},
        {"language": "English", "proficiency": "Fluent", "level": "C1"},
        {"language": "German", "proficiency": "Basic", "level": "A2"},
        {"language": "French", "proficiency": "Basic", "level": "A2"},
        {"language": "Italian", "proficiency": "Basic", "level": "A2"}
    ]
    return languages

def get_technical_skills():
    """
    Retrieves technical skills and certifications for Cesar Cardoso.
    """
    skills = {
        "technical_languages_certifications": [
            "SAP/ABAP NetWeaver '04 Certification",
            "Ruby On Rails Show Day - Impacta"
        ],
        "agile_framework": [
            "SCRUM Agile for project management - Clarify"
        ],
        "software_development": "NodeJS, React, MongoDB, Firebase, PHP, ASP.NET, CSS, Javascript, Adobe Flex, MySql, SQL Server, Oracle, PySpark, Pandas, NumPy",
        "data_engineering": "GCP (Functions, BigQuery, Storage), SQL, Python (PySpark, Pandas, NumPy)",
        "project_management": "Agile, SCRUM"
    }
    return skills

def get_summary_and_competencies():
    """
    Retrieves a summary and competencies for Cesar Cardoso.
    """
    return {
        "summary": "AI Data Engineer | Project Manager | Developer",
        "personal_attributes": "analytic. creative. organized. people driven.",
        "management_competencies": "Management competencies, Software development, Software Engineer, Data Engineer, Communication and trust are the keys to excellent services, successful projects, robust products and foundation for resilient teams.",
        "expertise_years": "15 Years Development and Project expertise"
    }

def get_all_info():
    """
    Retrieves all information for Cesar Cardoso.
    """
    return {
        "contact_info": get_contact_info(),
        "professional_experience": get_professional_experience(),
        "education_info": get_education_info(),
        "sabbatical_experience": get_sabbatical_experience(),
        "languages": get_languages(),
        "technical_skills": get_technical_skills(),
        "summary_and_competencies": get_summary_and_competencies()
    }


def get_websites() -> dict:
    """Retrieves a list of available websites.

    Returns:
        dict: website url and description or error msg.
    """
    return {
        "status": "success",
        "websites": [
            {
                "url": "https://cesarbouli.com",
                "description": "A website for composer Cesar Bouli",
            },
            {
                "url": "https://byeceebee.com",
                "description": "Website for electronic music experiments by Cesar Bouli",
            },
            {
                "url": "https://github.com/cesarbouli",
                "description": "Github profile for composer Cesar Bouli",
            },
            {
                "url": "https://www.linkedin.com/in/cesardesouzacardoso/",
                "description": "Linkedin profile for Cesar Bouli, real name Cesar Cardoso",
            },
            {
                "url": "https://www.youtube.com/@CesarBouli",
                "description": "Youtube channel for composer Cesar Bouli",
            },
            {
                "url": "https://www.instagram.com/cesarbouli/",
                "description": "Instagram profile for composer Cesar Bouli",
            },
            {
                "url": "https://www.youtube.com/@canalguitah",
                "description": "Youtube channel with information about guitars",
            },
        ],
    }



root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the Cesar Bouli."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about Cesar Bouli, a Brazilian composer and programmer."
    ),
    tools=[get_websites, get_all_info],
)
