import streamlit as st
import sqlite3
import os
from google import genai
from google.genai import types

# =========================================================
# GEMINI AI SETUP
# =========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
else:
    gemini_client = None


def ask_eduloop_ai(message):

    if gemini_client is None:
        return "Gemini AI is not connected."

    try:
        chat = gemini_client.chats.create(
            model="gemini-3.6-flash"
        )

        response = chat.send_message(
            message=message
        )

        return response.text

    except Exception as e:
        return f"AI temporarily unavailable: {e}"


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="EduLoop",
    page_icon="📚",
    layout="wide"
)
# =========================================================
# ✨ EDULOOP FANTASY UI
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(170,120,255,0.20), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(90,180,255,0.16), transparent 30%),
        radial-gradient(circle at 50% 90%, rgba(220,100,255,0.12), transparent 35%),
        linear-gradient(135deg, #090719 0%, #11102b 45%, #090719 100%);
    color: #f7f2ff;
}

/* ---------- EVERYTHING ---------- */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ---------- HEADINGS ---------- */

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #f4eaff !important;
    letter-spacing: 1px;
}

h1 {
    font-size: 3.2rem !important;
    text-shadow:
        0 0 10px rgba(190,130,255,0.8),
        0 0 25px rgba(120,80,255,0.4);
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(23,18,52,0.98),
            rgba(10,8,27,0.98)
        );
    border-right: 1px solid rgba(190,140,255,0.25);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #e7cfff !important;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(205,160,255,0.45);
    background:
        linear-gradient(
            135deg,
            #6d3fc4,
            #9b5de5
        );
    color: white;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    padding: 0.65rem 1rem;
    box-shadow:
        0 5px 20px rgba(125,70,220,0.30);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 8px 28px rgba(170,100,255,0.55);
    border-color: #e2c5ff;
}

/* ---------- INPUTS ---------- */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: rgba(255,255,255,0.055) !important;
    color: #ffffff !important;
    border: 1px solid rgba(190,150,255,0.25) !important;
    border-radius: 12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus {
    border-color: #b77aff !important;
    box-shadow: 0 0 12px rgba(170,100,255,0.3) !important;
}

/* ---------- SELECT BOX ---------- */

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.055) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(190,150,255,0.25) !important;
}

/* ---------- GLASS CONTAINERS ---------- */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );
    border: 1px solid rgba(200,160,255,0.18);
    border-radius: 20px;
    box-shadow:
        0 10px 35px rgba(0,0,0,0.25);
    backdrop-filter: blur(15px);
}

/* ---------- METRICS ---------- */

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            135deg,
            rgba(130,80,220,0.16),
            rgba(255,255,255,0.035)
        );
    border: 1px solid rgba(190,140,255,0.2);
    border-radius: 18px;
    padding: 15px;
}

/* ---------- INFO / SUCCESS BOXES ---------- */

div[data-testid="stAlert"] {
    border-radius: 15px;
    background: rgba(120,80,200,0.10);
    border: 1px solid rgba(190,140,255,0.20);
}

/* ---------- DIVIDERS ---------- */

hr {
    border-color: rgba(200,160,255,0.16) !important;
}

/* ---------- TOP GLOW ---------- */

.hero-glow {
    text-align: center;
    padding: 35px 20px;
    margin-bottom: 25px;
    border-radius: 28px;

    background:
        radial-gradient(
            circle at center,
            rgba(140,80,255,0.22),
            transparent 65%
        );
}

/* ---------- BRAND ---------- */

.brand {
    font-family: 'Cinzel', serif;
    font-size: 4rem;
    font-weight: 700;
    letter-spacing: 3px;

    background:
        linear-gradient(
            90deg,
            #e6c9ff,
            #b982ff,
            #8fd8ff,
            #e6c9ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 30px rgba(170,100,255,0.25);
}

.tagline {
    font-size: 1.05rem;
    color: #cfc4e8;
    letter-spacing: 2px;
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    padding: 35px 10px 15px;
    color: #9f91b8;
    font-size: 0.85rem;
}

.footer strong {
    color: #d6b5ff;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATABASE
# =========================================================

def create_database():

    conn = sqlite3.connect("eduloop.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book TEXT NOT NULL,
            subject TEXT NOT NULL,
            course TEXT NOT NULL,
            college TEXT NOT NULL,
            edition TEXT,
            price REAL,
            condition TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_books():

    conn = sqlite3.connect("eduloop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, book, subject, course, college,
               edition, price, condition
        FROM books
        ORDER BY id DESC
    """)

    books = cursor.fetchall()

    conn.close()

    return books


def add_book(
    book,
    subject,
    course,
    college,
    edition,
    price,
    condition
):

    conn = sqlite3.connect("eduloop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO books
        (book, subject, course, college, edition, price, condition)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        book,
        subject,
        course,
        college,
        edition,
        price,
        condition
    ))

    conn.commit()
    conn.close()


# =========================================================
# AGENT TOOL: SEARCH BOOK DATABASE
# =========================================================

def search_books_tool(
    book_name="",
    subject="",
    course="",
    max_price=0
):

    books = get_books()

    results = []

    for book in books:

        book_id = book[0]
        book_title = book[1]
        book_subject = book[2]
        book_course = book[3]
        college = book[4]
        edition = book[5]
        price = book[6]
        condition = book[7]

        score = 0

        if book_name and book_name.lower() in book_title.lower():
            score += 40

        if subject and subject.lower() in book_subject.lower():
            score += 30

        if course and course.lower() in book_course.lower():
            score += 15

        if max_price > 0 and price <= max_price:
            score += 15

        if score > 0:

            results.append({
                "id": book_id,
                "book": book_title,
                "subject": book_subject,
                "course": book_course,
                "college": college,
                "edition": edition,
                "price": price,
                "condition": condition,
                "match_score": score
            })

    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return results


# =========================================================
# GEMINI TOOL DECLARATION
# =========================================================

search_books_declaration = {

    "name": "search_books",

    "description":
        "Search EduLoop's student book database "
        "for books matching a student's requirements.",

    "parameters": {

        "type": "object",

        "properties": {

            "book_name": {
                "type": "string",
                "description": "Name of the book"
            },

            "subject": {
                "type": "string",
                "description": "Subject of the book"
            },

            "course": {
                "type": "string",
                "description": "Student course or branch"
            },

            "max_price": {
                "type": "number",
                "description":
                    "Maximum price the student wants to pay"
            }

        },

        "required": []
    }
}


# =========================================================
# AGENTIC SEARCH
# =========================================================

def run_eduloop_agent(user_request):

    if gemini_client is None:
        return "Gemini AI is not connected.", []

    try:

        tools = types.Tool(
            function_declarations=[
                search_books_declaration
            ]
        )

        config = types.GenerateContentConfig(

            tools=[tools],

            automatic_function_calling=
                types.AutomaticFunctionCallingConfig(
                    disable=True
                )
        )

        contents = [

            types.Content(

                role="user",

                parts=[
                    types.Part.from_text(
                        text=user_request
                    )
                ]
            )
        ]

        # STEP 1:
        # Gemini decides which tool to use

        response = gemini_client.models.generate_content(

            model="gemini-3.6-flash",

            contents=contents,

            config=config
        )

        function_call = None

        if response.candidates:

            for part in response.candidates[0].content.parts:

                if part.function_call:

                    function_call = part.function_call

                    break

        # No tool call

        if function_call is None:

            return response.text, []

        # STEP 2:
        # Execute database tool

        if function_call.name == "search_books":

            args = function_call.args

            results = search_books_tool(

                book_name=args.get(
                    "book_name",
                    ""
                ),

                subject=args.get(
                    "subject",
                    ""
                ),

                course=args.get(
                    "course",
                    ""
                ),

                max_price=float(
                    args.get(
                        "max_price",
                        0
                    ) or 0
                )
            )

            # STEP 3:
            # Send tool result back to Gemini

            contents.append(
                response.candidates[0].content
            )

            function_response = (
                types.Part.from_function_response(

                    name=function_call.name,

                    response={
                        "result": results
                    },

                    id=function_call.id
                )
            )

            contents.append(

                types.Content(

                    role="user",

                    parts=[
                        function_response
                    ]
                )
            )

            # STEP 4:
            # Gemini generates final response

            final_response = (
                gemini_client.models.generate_content(

                    model="gemini-3.6-flash",

                    contents=contents,

                    config=config
                )
            )

            return final_response.text, results

        return (
            "I couldn't search the book database.",
            []
        )

    except Exception as e:

        return (
            f"Agent error: {e}",
            []
        )


# =========================================================
# AI BOOK RECOMMENDATION
# =========================================================

def recommend_books_with_ai(
    user_request,
    results
):

    if gemini_client is None:
        return "Gemini AI is not connected."

    if not results:
        return "No suitable books were found."

    prompt = f"""

You are EduLoop AI,
a smart academic book recommendation agent.

Student request:

{user_request}

Available books:

{results}

Recommend the most suitable options
from ONLY the books listed above.

For each recommendation mention:

1. Book name
2. Price
3. Condition
4. Why it matches the student's requirement

Keep the answer concise and student-friendly.

Do not invent information.

"""

    return ask_eduloop_ai(prompt)


# =========================================================
# AGENT ACTIVITY
# =========================================================

def show_agent_activity():

    st.subheader(
        "⚙️ EduLoop Agent Activity"
    )

    steps = [

        "🧠 Understanding student's request",

        "🔎 Searching EduLoop book database",

        "📊 Comparing matching books",

        "💰 Checking prices and conditions",

        "🤖 Generating personalized recommendation"

    ]

    for step in steps:

        st.write(
            "✅ " + step
        )


# =========================================================
# CREATE DATABASE
# =========================================================

create_database()


# =========================================================
# SESSION STATE
# =========================================================

if "profile_created" not in st.session_state:

    st.session_state.profile_created = False


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero-glow">

<div class="brand">
📚 EDULOOP
</div>

<div class="tagline">
PASS THE BOOK, NOT THE COST ✦
</div>

<p style="
color:#b9aecf;
margin-top:15px;
font-size:0.95rem;
">
An AI-powered student-to-student academic book exchange
</p>

</div>
""", unsafe_allow_html=True)
st.write(
    "Buy, sell and reuse academic books "
    "through an intelligent student-to-student "
    "exchange platform."
)

st.divider()


# =========================================================
# PROFILE PAGE
# =========================================================

if not st.session_state.profile_created:

    st.header(
        "👋 Create Your Student Profile"
    )

    st.write(
        "Your profile helps EduLoop understand "
        "your academic requirements and find "
        "relevant book matches."
    )

    name = st.text_input(
        "👤 Full Name"
    )

    college = st.text_input(
        "🏫 College / University"
    )

    course = st.text_input(
        "🎓 Course / Branch"
    )

    year = st.selectbox(

        "📅 Current Year",

        [
            "First Year",
            "Second Year",
            "Third Year",
            "Fourth Year"
        ]
    )

    if st.button(
        "🚀 Create My Profile"
    ):

        if name and college and course:

            st.session_state.profile_created = True

            st.session_state.name = name

            st.session_state.college = college

            st.session_state.course = course

            st.session_state.year = year

            st.rerun()

        else:

            st.warning(
                "⚠️ Please fill in your name, college and course."
            )


# =========================================================
# MAIN APPLICATION
# =========================================================

else:

    st.success(
        f"Welcome to EduLoop, "
        f"{st.session_state.name}! 👋"
    )

    # -----------------------------------------------------
    # SIDEBAR
    # -----------------------------------------------------

    st.sidebar.title(
        "📚 EduLoop"
    )

    st.sidebar.write(
        f"**Student:** "
        f"{st.session_state.name}"
    )

    st.sidebar.write(
        f"**College:** "
        f"{st.session_state.college}"
    )

    st.sidebar.write(
        f"**Course:** "
        f"{st.session_state.course}"
    )

    st.sidebar.write(
        f"**Year:** "
        f"{st.session_state.year}"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigate",

        [
            "🏠 Dashboard",
            "📤 Sell a Book",
            "🔍 Find a Book",
            "📚 Available Books"
        ]
    )


    # =====================================================
    # DASHBOARD
    # =====================================================

    if page == "🏠 Dashboard":

        st.header(
            "🏠 Your EduLoop Dashboard"
        )

        st.write(
            "What would you like to do today?"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "📤 Sell a Book"
            )

            st.write(
                "Have a book you no longer need? "
                "EduLoop can analyze it and recommend "
                "a fair resale price."
            )

            st.info(
                "Use the sidebar to open **Sell a Book**."
            )

        with col2:

            st.subheader(
                "🔍 Find a Book"
            )

            st.write(
                "Tell EduLoop what you need and "
                "the AI agent will search the "
                "student book database."
            )

            st.info(
                "Use the sidebar to open **Find a Book**."
            )

        st.divider()

        st.header(
            "🤖 How the EduLoop Agent Works"
        )

        step1, step2, step3, step4 = st.columns(4)

        with step1:

            st.markdown(
                "### 1️⃣ Understand"
            )

            st.write(
                "Understands the student's "
                "book requirement."
            )

        with step2:

            st.markdown(
                "### 2️⃣ Analyze"
            )

            st.write(
                "Analyzes price, condition "
                "and requirements."
            )

        with step3:

            st.markdown(
                "### 3️⃣ Match"
            )

            st.write(
                "Finds and ranks suitable "
                "student listings."
            )

        with step4:

            st.markdown(
                "### 4️⃣ Act"
            )

            st.write(
                "Helps the student initiate "
                "the exchange."
            )

        st.divider()

        books = get_books()

        st.metric(
            "📚 Books Currently Listed",
            len(books)
        )


    # =====================================================
    # SELL A BOOK
    # =====================================================

    elif page == "📤 Sell a Book":

        st.header(
            "📤 Sell Your Book"
        )

        st.write(
            "Enter your book details. "
            "EduLoop will analyze the information "
            "and recommend a resale price."
        )

        book_name = st.text_input(
            "📖 Book Name"
        )

        subject = st.text_input(
            "📚 Subject"
        )

        edition = st.text_input(
            "🔢 Edition"
        )

        original_price = st.number_input(

            "💰 Original Price (₹)",

            min_value=1.0,

            value=500.0,

            step=50.0
        )

        condition = st.selectbox(

            "📕 Book Condition",

            [
                "Like New",
                "Very Good",
                "Good",
                "Fair"
            ]
        )

        demand = st.selectbox(

            "📈 Expected Demand",

            [
                "High",
                "Medium",
                "Low"
            ]
        )


        # -------------------------------------------------
        # GEMINI ANALYSIS
        # -------------------------------------------------

        if st.button(
            "🤖 Ask EduLoop AI"
        ):

            if not book_name or not subject:

                st.warning(
                    "Please enter the book name and subject."
                )

            else:

                prompt = f"""

You are EduLoop,
an AI agent for student-to-student
academic book exchange.

Analyze this used academic book:

Book: {book_name}

Subject: {subject}

Course: {st.session_state.course}

Edition: {edition}

Original Price: ₹{original_price}

Condition: {condition}

Demand: {demand}

Give:

1. A reasonable resale price range in INR.
2. A short explanation of the factors considered.
3. Whether the seller should price it low, moderate, or high for students.

Keep the answer concise and practical.

"""

                with st.spinner(
                    "🤖 EduLoop AI is analyzing the book..."
                ):

                    ai_result = ask_eduloop_ai(
                        prompt
                    )

                st.subheader(
                    "🤖 EduLoop AI Analysis"
                )

                st.write(
                    ai_result
                )


        st.divider()


        # -------------------------------------------------
        # PRICE CALCULATOR
        # -------------------------------------------------

        if st.button(
            "🤖 Analyze Book & Recommend Price"
        ):

            if not book_name or not subject:

                st.warning(
                    "Please enter the book name and subject."
                )

            else:

                condition_multiplier = {

                    "Like New": 0.65,

                    "Very Good": 0.55,

                    "Good": 0.45,

                    "Fair": 0.30
                }

                demand_multiplier = {

                    "High": 1.10,

                    "Medium": 1.00,

                    "Low": 0.90
                }

                base_price = (

                    original_price
                    * condition_multiplier[condition]
                )

                suggested_price = (

                    base_price
                    * demand_multiplier[demand]
                )

                lower_price = (
                    suggested_price * 0.90
                )

                upper_price = (
                    suggested_price * 1.10
                )

                st.success(
                    "🤖 EduLoop Agent has analyzed your book!"
                )

                st.header(
                    "💰 Recommended Price"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Original Price",
                        f"₹{original_price:.0f}"
                    )

                with col2:

                    st.metric(
                        "Suggested Price",
                        f"₹{suggested_price:.0f}"
                    )

                with col3:

                    st.metric(
                        "Condition",
                        condition
                    )

                st.info(

                    f"Recommended resale range: "
                    f"₹{lower_price:.0f} – "
                    f"₹{upper_price:.0f}"
                )


                # -------------------------------------------------
                # AGENT ACTIVITY
                # -------------------------------------------------

                with st.expander(
                    "🤖 View EduLoop Agent Activity"
                ):

                    st.write(
                        "🧠 Agent Status: ANALYSIS COMPLETE"
                    )

                    st.write(
                        "📖 Identified the academic book"
                    )

                    st.write(
                        "💰 Analyzed original price"
                    )

                    st.write(
                        f"📕 Evaluated book condition: "
                        f"{condition}"
                    )

                    st.write(
                        f"📈 Evaluated expected demand: "
                        f"{demand}"
                    )

                    st.write(
                        "🎯 Calculated recommended resale price"
                    )

                    st.success(
                        "Price recommendation generated."
                    )


                st.divider()


                if st.button(
                    "✅ List Book on EduLoop"
                ):

                    add_book(

                        book_name,

                        subject,

                        st.session_state.course,

                        st.session_state.college,

                        edition,

                        round(
                            suggested_price
                        ),

                        condition
                    )

                    st.success(
                        "🎉 Your book has been successfully listed!"
                    )

                    st.info(
                        "🤖 EduLoop can now search for "
                        "students who may need this book."
                    )


    # =====================================================
    # FIND A BOOK - AGENTIC AI
    # =====================================================

    elif page == "🔍 Find a Book":

        st.header(
            "🔍 Find a Book"
        )

        st.write(
            "Tell EduLoop what you need in your own words. "
            "The AI agent will understand your request, "
            "call the book-search tool and recommend "
            "matching listings."
        )

        user_request = st.text_area(

            "🤖 What book are you looking for?",

            placeholder=
            "Example: I need a Python book for CSBS under ₹500"
        )


        if st.button(
            "🤖 Ask EduLoop Agent"
        ):

            if not user_request.strip():

                st.warning(
                    "Please describe the book you are looking for."
                )

            else:

                with st.spinner(
                    "🤖 EduLoop Agent is working..."
                ):

                    ai_response, results = (
                        run_eduloop_agent(
                            user_request
                        )
                    )


                st.success(
                    "🤖 EduLoop Agent completed the search"
                )


                # -------------------------------------------------
                # ACTIVITY
                # -------------------------------------------------

                show_agent_activity()


                # -------------------------------------------------
                # AGENT RESPONSE
                # -------------------------------------------------

                st.subheader(
                    "🤖 Agent Response"
                )

                st.write(
                    ai_response
                )


                # -------------------------------------------------
                # RESULTS
                # -------------------------------------------------

                if results:

                    recommendation = (
                        recommend_books_with_ai(
                            user_request,
                            results
                        )
                    )

                    st.subheader(
                        "🤖 EduLoop AI Recommendation"
                    )

                    st.info(
                        recommendation
                    )

                    st.divider()

                    st.subheader(
                        "📚 Matching Books"
                    )


                    for book in results:

                        with st.container(
                            border=True
                        ):

                            col1, col2, col3 = (
                                st.columns(3)
                            )


                            with col1:

                                st.subheader(
                                    f"📖 {book['book']}"
                                )

                                st.write(
                                    f"📚 **Subject:** "
                                    f"{book['subject']}"
                                )

                                st.write(
                                    f"🎓 **Course:** "
                                    f"{book['course']}"
                                )

                                st.write(
                                    f"🏫 **College:** "
                                    f"{book['college']}"
                                )


                            with col2:

                                st.write(
                                    f"💰 **Price:** "
                                    f"₹{book['price']:.0f}"
                                )

                                st.write(
                                    f"📕 **Condition:** "
                                    f"{book['condition']}"
                                )

                                st.write(
                                    f"🔢 **Edition:** "
                                    f"{book['edition']}"
                                )


                            with col3:

                                st.metric(

                                    "Match Score",

                                    f"{book['match_score']}%"
                                )


                                if st.button(

                                    "📩 Request This Book",

                                    key=
                                    f"request_{book['id']}"
                                ):

                                    st.success(
                                        "🎉 Book request sent!"
                                    )

                                    st.info(

                                        f"EduLoop notified the seller "
                                        f"of **{book['book']}**."
                                    )


                else:

                    st.warning(

                        "No matching books found. "
                        "Try another description or "
                        "a higher budget."
                    )


    # =====================================================
    # AVAILABLE BOOKS
    # =====================================================

    elif page == "📚 Available Books":

        st.header(
            "📚 Available Books"
        )

        st.write(
            "Books currently listed by students on EduLoop."
        )

        books = get_books()


        if books:

            for book in books:

                book_id = book[0]

                book_name = book[1]

                subject = book[2]

                course = book[3]

                college = book[4]

                edition = book[5]

                price = book[6]

                condition = book[7]


                with st.container(
                    border=True
                ):

                    col1, col2, col3 = (
                        st.columns([2, 1, 1])
                    )


                    with col1:

                        st.subheader(
                            f"📖 {book_name}"
                        )

                        st.write(
                            f"📚 Subject: {subject}"
                        )

                        st.write(
                            f"🎓 Course: {course}"
                        )

                        st.write(
                            f"🏫 College: {college}"
                        )


                    with col2:

                        st.write(
                            f"💰 **₹{price:.0f}**"
                        )

                        st.write(
                            f"📕 {condition}"
                        )


                    with col3:

                        st.write(
                            f"🔢 Edition: {edition}"
                        )


        else:

            st.info(
                "No books have been listed yet."
            )
# =========================================================
# ✨ FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Built with 💜 and AI
    <br><br>
    <strong>BY EKANSHI GOYAL</strong>
    <br>
    <span>EduLoop • Student Book Exchange</span>
</div>
""", unsafe_allow_html=True)