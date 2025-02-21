from datetime import datetime
class Note:#base class
    '''
    It initializes new notes
    '''
    def __init__(self, note_id, content, created_at):
        self.note_id = note_id # Notes_id
        self.content = content # it contains the contents in the notes
        self.created_at = created_at #store the created time stamp
class TextNote(Note): #Child class
    def __init__(self, note_id, content, created_at=None):
        if created_at is None:
            created_at = datetime.now() # time the note was created
        Note.__init__(self, note_id, content, created_at)# initializing the parent class
    def display(self):# function to display code in the textnote class
      '''
      Display the details of notes
      '''
      return f"ID:{self.note_id}, {self.content} was created at {self.created_at}"
class ReminderNote(Note): #Child class
    def __init__(self, note_id, content, created_at, reminder_date, time):
        Note.__init__(self, note_id, content, created_at)
        self.reminder_date = reminder_date
        self.time = time
    def display(self):
        return f"ID:{self.note_id}, {self.content} was created at {self.created_at}, reminder is set for {self.reminder_date} at {self.time}"
class NotesManager:
    def __init__(self):
        self.notes = [] # this stores the notes in a list for easy access
        self.nextid = 1  # initial id count

    def add_note(self, note_type, content, reminder_date=None, time=None): # function to add data to the notes class
        note_id = self.nextid
        '''
        Conditional loop for adding data to the list of not_es.
        '''
        if note_type == "Text":
            note = TextNote(note_id, content, created_at=datetime.now())
        elif note_type == "Reminder":
            note = ReminderNote(note_id, content, created_at=datetime.now(), reminder_date=reminder_date, time=time)
        else:
            raise ValueError("Wrong note type")
        self.notes.append(note)
        self.nextid += 1
    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                break  # added break to stop the loop once the note is found
        else:
            print("ERROR! Note ID not found")
        '''
        This block of conditional loop would return return the next id to 1 after \n
        everything in the notesmanager has been deleted"
        '''
        if self.notes:
            self.nextid = max(note.note_id for note in self.notes) + 1
        else:
            self.nextid = 1
#function to display notes
    def show_notes(self):
        for note in self.notes:
            print(note.display())

    def search_notes(self, keyword):
        for note in self.notes:
            if keyword in note.content:
                print(note.display())
            else:
                print("The keyword cannot be found in the lists of notes")
my_notes = NotesManager()
def main():# main function to run the code
    while True: # while loop
        """
        Print statement indicating viable user prompts
            1: To add notes
            2: To search notes
            3: To Delete notes
            4: To Show notes
        """
        print("ENTER A LIST OF THINGS YOU WANT TO DO:")
        print("1: Add note")
        print("2: Search note")
        print("3: Delete note")
        print("4: Show notes")
        print("5: Exit")
        choice = input("Enter your choice: ")
            #conditional loop for executing these commands
        if choice == '1':
            note_type = input("Enter note type (Text/Reminder): ")
            content = input("Enter note content: ")
            if note_type == "Reminder":
                reminder_date = input("Enter reminder date (YYYY-MM-DD): ")
                time = input("Enter reminder time (HH:MM): ")
                my_notes.add_note(note_type, content, reminder_date, time)
            else:
                my_notes.add_note(note_type, content)
        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            my_notes.search_notes(keyword)
        elif choice == '3':
            note_id = int(input("Enter note ID to delete: "))
            my_notes.delete_note(note_id)
        elif choice == '4':
            my_notes.show_notes()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()# calling the main function for executing the program