import random

words = {
    "안녕하세요": "Hello",
    "사랑": "Love",
    "사람": "Person",
    "집": "House",
    "물": "Water",
    "밥": "Rice",
    "차": "Car/Tea",
    "학교": "School",
    "친구": "Friend",
    "책": "Book",
    "날씨": "Weather",
    "시간": "Time",
    "고양이": "Cat",
    "강아지": "Dog",
    "컴퓨터": "Computer",
    "전화": "Phone",
    "음악": "Music",
    "영화": "Movie",
    "생일": "Birthday",
    "아버지": "Father",
    "어머니": "Mother",
    "형제": "Brother",
    "자매": "Sister",
    "교수": "Professor",
    "학생": "Student",
    "선생님": "Teacher",
    "의사": "Doctor",
    "간호사": "Nurse",
    "경찰": "Police",
    "소방관": "Firefighter",
    "병원": "Hospital",
    "약국": "Pharmacy",
    "은행": "Bank",
    "가게": "Store",
    "시장": "Market",
    "음식": "Food",
    "커피": "Coffee",
    "차": "Tea",
    "맥주": "Beer",
    "포도주": "Wine",
    "술": "Alcohol",
    "가족": "Family",
    "친척": "Relative",
    "이웃": "Neighbor",
    "동네": "Neighborhood",
    "도시": "City",
    "나라": "Country",
    "세계": "World",
    "하늘": "Sky",
    "별": "Star",
    "달": "Moon",
    "태양": "Sun",
    "비": "Rain",
    "눈": "Snow",
    "바람": "Wind",
    "산": "Mountain",
    "강": "River",
    "바다": "Sea",
    "호수": "Lake",
    "섬": "Island",
    "숲": "Forest",
    "나무": "Tree",
    "꽃": "Flower",
    "새": "Bird",
    "물고기": "Fish",
    "곤충": "Insect",
    "사자": "Lion",
    "호랑이": "Tiger",
    "코끼리": "Elephant",
    "원숭이": "Monkey",
    "말": "Horse",
    "돼지": "Pig",
    "소": "Cow",
    "양": "Sheep",
    "닭": "Chicken",
    "계란": "Egg",
    "빵": "Bread",
    "버터": "Butter",
    "치즈": "Cheese",
    "과일": "Fruit",
    "야채": "Vegetable",
    "사과": "Apple",
    "바나나": "Banana",
    "딸기": "Strawberry",
    "포도": "Grape",
    "오렌지": "Orange",
    "수박": "Watermelon",
    "멜론": "Melon",
    "토마토": "Tomato",
    "감자": "Potato",
    "양파": "Onion",
    "당근": "Carrot",
    "고추": "Pepper",
    "마늘": "Garlic",
    "생강": "Ginger",
    "소금": "Salt",
    "설탕": "Sugar",
    "후추": "Pepper",
    "양념": "Spice",
    "식초": "Vinegar"
}

def quiz_user(words):
     words_list = list(words.items())
     random.shuffle(words_list)
     score = 0

     for korean, english in words_list:
        print(f"What is the English translation of '{korean}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = english.lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{english}'.\n")


     print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz..")
    quiz_user(words)


if __name__ == "__main__":
    main()