from response import generate_response

def reinforcement_learning_activity():
    print("\nREINFORCEMENT LEARNING ACTIVITY\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ").strip()
    if not prompt:
        print("Enter a prompt to begin")
        return
    
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")
    try:
        rating = int(input("Rate the response from 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating = 3
    except ValueError:
        print("invalid rating. Using 3.")
        rating = 3
        
    feedback = input("Provide some feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Improved with the feedback: {feedback})"
    print(f"\nImproved AI Response: {improved_response}")
    
    print("\nReflection:")
    print("1. how did the model help shape the AI's response?")
    print("2. How could this help improve the AI's response")
    
def role_based_prompt():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math: )").strip()
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ").strip()
        
    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
        
    educator_prompt = f"You are an educator. Explain {item} in simple terms."
    professor_prompt = f"You are an professor in {category}. Explain {item} in a detailed, technical manner."
        
    educator_response = generate_response(educator_prompt, temperature=0.3, max_tokens=1024)
    professor_response = generate_response(professor_prompt, temperature=0.3, max_tokens=1024)
        
    print(f"\n--- Educator's Perspective ---\n{educator_response}") 
    print(f"\n--- Professor's Perspective ---\n{professor_response}")
        
    print("\nReflection:")
    print("1. How did the output vary from the educator and professor perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")
        
def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity: ")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()
    
    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        
if __name__ == "__main__":
    run_activity()