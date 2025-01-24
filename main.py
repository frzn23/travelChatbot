import openai
from env import API_KEY


def get_openai_response(prompt):
    
    # Function to interact with OpenAI API using the updated chat completions format.
    openai.api_key = API_KEY
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": """You are a professional travel agent creating a personalized travel itinerary for a client."""},
                {
                    "role": "user",
                    "content": prompt
                }
            ],

        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def gather_user_preferences():
    # Function to gather basic user inputs
    print("Welcome to the Travel Itinerary Generator!")
    user_input = {
        "destination": input("Enter your travel destination: "),
        "budget": input("Enter your budget (e.g., low, moderate, luxury): "),
        "trip_duration": input("Enter the duration of your trip in days: "),
        "purpose": input("Enter the purpose of your trip (e.g., leisure, adventure, business): "),
        "preferences": input("Enter any specific preferences (e.g., food, culture, nature): ")
    }
    return user_input

def refine_preferences(user_input):
    # Function to refine user preferences by asking follow-up questions
    prompt = (
        f"The user provided the following details: \n"
        f"Destination: {user_input['destination']}\n"
        f"Budget: {user_input['budget']}\n"
        f"Trip Duration: {user_input['trip_duration']} days\n"
        f"Purpose: {user_input['purpose']}\n"
        f"Preferences: {user_input['preferences']}\n"
        f"Ask any necessary clarifying questions to refine the itinerary."
    )
    response = get_openai_response(prompt)
    print("\nTo refine your itinerary, please answer the following:")
    print(response)
    user_input["refinements"] = input("Your response: ")
    return user_input

def generate_itinerary(user_input):
    # Function to generate a travel itinerary based on user inputs
    prompt = (
        f"Generate a detailed day-by-day travel itinerary for the following user details: \n"
        f"Destination: {user_input['destination']}\n"
        f"Budget: {user_input['budget']}\n"
        f"Trip Duration: {user_input['trip_duration']} days\n"
        f"Purpose: {user_input['purpose']}\n"
        f"Preferences: {user_input['preferences']}\n"
        f"Refinements: {user_input.get('refinements', '')}"
    )
    response = get_openai_response(prompt)
    return response

def main():
    # Main function to execute the prompt system
    user_input = gather_user_preferences()
    user_input = refine_preferences(user_input)
    itinerary = generate_itinerary(user_input)
    print("\nHere is your personalized travel itinerary:")
    print(itinerary)

if __name__ == "__main__":
    main()
