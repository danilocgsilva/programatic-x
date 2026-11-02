from programatic_x.factory.ButtonStartFactory import ButtonStartFactory

def main():
    print("Starting automated start button click...")
    
    button_start = ButtonStartFactory.create_button_start()
    
    try:
        button_start.click()
        print("Successfully clicked the start button!")
    except Exception as e:
        print(f"Failed to click start button: {e}")

if __name__ == "__main__":
    main()