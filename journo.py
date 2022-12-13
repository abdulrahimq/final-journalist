import os
import openai
import re


openai.api_key = os.environ['OPENAI_KEY']


paragraph = "TEMPLATE TEXT"

prompts_dict = {
    "headline": f'''
Write a headline for the following article for the New York Times:				

The Brady-Johnson Program in Grand Strategy is one of Yale University’s most celebrated and prestigious programs. Over the course of a year, it allows a select group of about two dozen students to immerse themselves in classic texts of history and statecraft, while also rubbing shoulders with guest instructors drawn from the worlds of government, politics, military affairs and the media. But now, a program created to train future leaders how to steer through the turbulent waters of history is facing a crisis of its own. Beverly Gage, a historian of 20th-century politics who has led the program since 2017, has resigned, saying the university failed to stand up for academic freedom amid inappropriate efforts by its donors to influence its curriculum and faculty hiring.
Headline: Leader of Prestigious Yale Program Resigns, Citing Donor Pressure
------------

Write a headline for the follwoing article for The Atlantic:

When Bobby McIlvaine died on September 11, 2001, his desk at home was a study in plate tectonics, coated in shifting piles of leather-bound diaries and yellow legal pads. He’d kept the diaries since he was a teenager, and they were filled with the usual diary things—longings, observations, frustrations—while the legal pads were marbled with more variety: aphoristic musings, quotes that spoke to him, stabs at fiction.
Headline: What Bobby McIlvaine Left Behind 

-----------

Write a headline for the follwoing article for Longreads.com:
There were seven of them. Their names were Ananda-Lahari, Andrea, Harita, Stutisheel, Takusumi, Vasu, and Wei Ming. They each had different gaits. Takusumi ran with his knees bent inward, almost like a ritual. Stutisheel shuffled each foot against the sidewalk like he was scraping dogshit off the bottom of his shoes. Sometimes Wei Ming ran like a dancer, floating for a second before the descent. Andrea and Vasu clicked off rhythmic steps, as if borne from an assembly line. To watch them was to watch some invisible piano player timing their notes off of the rhythm of their footfall. By just the second time I arrived, each runner had run well over a hundred miles. They were not stopping soon.
Headline: Children on the Garden: On Life at a 3,100-Mile Race

-------------

Write a headline for the follwoing article for the Washington Post:
''',

    "interview_questions": f'''
	Create a list of questions for my interview with the CEO of a big corporate:

1. Do you believe there is a right or wrong when it comes to how companies function in the world, or is it all a matter of degree?
2. How would you characterize that disposition of a socially responsible C.E.O.? What are the attributes?
3. There are reasons your company has been a positive force in the world — chiefly economic ones but also ones having to do with personal pleasure. But inarguably some of those beneficial aspects have come at a cost to both human and environmental health. How did you think about those ethical trade-offs?
4. When you meet with business leaders today, is there anything you’re hearing that makes you think, gosh, these people are living in the past?
5. So let’s say you were running a company in Texas, and that company believed in the importance of supporting young families. What would the company’s thinking be around the state’s abortion laws?
6. But surely the issues you just described are connected to the ability to have a family when you want to have a family?
7. More generally, when it comes to corporate responses to political changes, what factors would you be looking at to help you determine the right response for your company?
8. How did your attitude about money change the further along you went in your career, once you became very handsomely compensated?
9. Do you think there is anything gendered to your decision to turn down a raise?
10. Did you feel as if you understood the blowback to the ad and agreed with it? Or was the blowback itself sufficient for you to feel you’d made a mistake?

------------

Create a list of questions for my interview with a cognitive psychologist, psycholinguist, popular science author and public intellectual: 

1. Your new book is driven by the idea that it would be good if more people thought more rationally. But people don’t think they’re irrational. So what mechanisms would induce more people to test their own thinking and beliefs for rationality?
2. Are there aspects of your own life in which you’re knowingly irrational?
3. Do you see any irrational beliefs as useful?
4. What about love?
5. I don’t think I’m alone in feeling that rising authoritarianism, the pandemic and the climate crisis, among other things, are signs that we’re going to hell in a handbasket. Is that irrational of me?
6. How can we know if the fights happening in academia over free speech — which you’ve experienced firsthand — are just the labor pains of new norms? And how do we then judge if those norms are ultimately positive or negative?
7. You said we have to look at whether or not new norms are designed to reward more accurate beliefs or marginalize less accurate ones. How does that apply to subjective issues like, for example, ones to do with identity?
8. What links do you see between rationality and morality?
9. If we agree that well-being is better than its opposite, where does economic equality fit in? Is that a core aspect of well-being?
10. Is it possible that the rising-tide-lifts-all-boats economic argument provides the wealthy with an undue moral cover for the self-interested inequality that their wealth grants them?

------
Create a list of questions for my interview with ''',

"article_outline": "Create an outline for a study on Factors Affecting the Infant Feeding Practices of Mothers in Las Pinas City:\n\n1: Statement of the Problem\n2: Definition of Terms\n3: Benefits of Breastfeeding\n4: WHO Recommendations\n5: The International Code of Marketing of Breast Milk Substitutes\n6: The Baby-Friendly Hospital Initiative\n7: Formula Feeding\n8: Socio-economic Demographic Profile of Mothers\n9: Previous Infant Feeding Practices\n10: Conclusion\n------------------------------------------------------------------------------------------------------------------------------\nCreate an outline for an essay about Asbestos Poisoning:\n1: Definition of Asbestos Poisoning\n2: Significance of the Study\n3: Symptoms of Asbestos Poisoning\n4: Effects of Asbestos Poisoning\n5: Treatments\n6: Conclusion\n7: Recommendations\n8: How to Deal with Asbestos Hazards\n------------------------------------------------------------------------------------------------------------------------------\nCreate an outline for an essay about Shakespeare:\n1: Introduction\n2: Early Life\n3: His Father\n4: His Mother\n5: Life of Anne Hathaway\n6: Reference in Shakespeare's Poems\n7: Plays\n8: Sonnets\n9: Other Poems\n10: His Later Years\n11: Conclusion\n------------------------------------------------------------------------------------------------------------------------------\nCreate an outline for a long-form article about ",
}


def preprocess_questions_list(q_list):
    temp_text = "1. " + q_list
    temp_text = re.split('([0-9][0-9]*\S)', temp_text)[1:-2]
    questions_result = []
    for i, j in zip(temp_text[::2], temp_text[1::2]):
        questions_result.append(i + j)
    return questions_result

def preprocess_outline_list(q_list):
    temp_text = "1. " + q_list
    temp_text = re.split('([0-9][0-9]*\S)', temp_text)[1:]
    questions_result = []
    for i, j in zip(temp_text[::2], temp_text[1::2]):
        questions_result.append(i + j)
    return questions_result

def generate_interview_question(max_tokens=100, paragraph=""):
    if not paragraph:
        paragraph = input(f'''Please enter the main paragraph\n-------------------------\n''')
    text = prompts_dict['interview_questions'] + f"{paragraph}:\n1."

    response = openai.Completion.create(
        engine="text-davinci-002",
        #engine="text-curie-001",
        prompt=text,
        max_tokens=max_tokens,
        temperature=0.8, top_p=1)
    results = preprocess_questions_list(response['choices'][0]['text'])
    return results


def generate_article_outline(max_tokens=150, paragraph=""):
    print("OUTLINE GENERATOR")
    if not paragraph:
        paragraph = input(f'''Please enter the main paragraph\n--------------------------\n''')
    text = prompts_dict['article_outline'] + f"{paragraph}:\n1:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        # engine="text-curie-001",
        prompt=text,
        temperature=0.3,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    results = preprocess_outline_list(response['choices'][0]["text"])
    return results


def generate_article_ideas(paragraph="", max_tokens=100) -> str:
    pass


def generate_headline(paragraph="", max_tokens=64) -> str:
    if not paragraph:
        paragraph = input(f'''Please enter the main paragraph\n-------------------------\n''')
    text = prompts_dict['headline'] + f"{paragraph}\n Headline: "

    response = openai.Completion.create(engine="text-curie-001", prompt=text, max_tokens=max_tokens,
                                        temperature=0.8, top_p=1)
    return response['choices'][0]['text']


def clean_prompt(prompt):
    prompt = prompt.replace("\n", " ")
    prompt = prompt.replace("\t", " ")
    return prompt


task_dict = {
    "interview_questions": generate_interview_question,
    "article_outline": generate_article_outline,
    "article_ideas": generate_article_ideas,
    "headline": generate_headline
}


def choose_generation(task_type="1"):
    num = input(f'''Please choose the number what type of text to generate: 
				1) Inteview Questions
				2) Article Outline
				3) Article Ideas
				4) Headline 
				''')
    tasks = {
        "1": "interview_questions",
        "2": "article_outline",
        "3": "article_ideas",
        "4": "headline"
    }
    name = tasks[num]
    return task_dict.get(name, lambda: 'Invalid')()


def parse_important_info(max_tokens=100):
    paragraph = input(f'''Please enter the main paragraph\n-------------------------\n''')
    text = f'''
Text: Outside the headquarters of Asaib Ahl al-Haq, one of the main Iranian-backed militias in Iraq, fighters have posted a giant banner showing the U.S. Capitol building swallowed up by red tents, symbols of a defining event in Shiite history. It’s election time in Iraq, and Asaib Ahl al-Haq — blamed for attacks on American forces and listed by the United States as a terrorist organization — is just one of the paramilitary factions whose political wings are likely to win Parliament seats in Sunday’s voting. The banner’s imagery of the 7th century Battle of Karbala and a contemporaneous quote pledging revenge sends a message to all who pass: militant defense of Shiite Islam. Eighteen years after the United States invaded Iraq and toppled a dictator, the run-up to the country’s fifth general election highlights a political system dominated by guns and money, and still largely divided along sectarian and ethnic lines.

Keywords: Iraq, Iran, Asaib Ahl al-Haq, Karbala, Shiite, Islam, United States

---------------------------------------------------------------------------------------------------

Text: Bitcoin’s proponents dream of a financial system largely free of government meddling. But the first time that cryptocurrency became a national currency, it was imposed on an unwilling population by an increasingly authoritarian ruler using a secretive state-run system. The surprising announcement last month that El Salvador had adopted bitcoin, the world’s largest cryptocurrency, as legal tender caught its population by surprise, and made the poor, conservative Central American nation an unlikely bellwether of a global technological transformation. The outcome of the uncharted experiment could help determine whether cryptocurrency delivers the freedom from regulation that its proponents envision — or whether it becomes another tool of control and enrichment for autocrats and corporations.

Keywords: Bitcoin, El Salvador, Central America, Cryptocurrency, Inflation, Technology

---------------------------------------------------------------------------------------------------

Text: {paragraph}

Keywords:'''
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=text,
        temperature=0.3,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response['choices'][0]['text']


def show_example(task_type: str) -> str:
    return prompts_dict[task_type]


if __name__ == "__main__":
    print("Journo app started")
