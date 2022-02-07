'''
Week 4 exercise
'''

class Email:
    """ An email with a list of recipients, a subject and a body. """

    def __init__(self, recipients, subject, body):
        """ (Email, list of Contact, str, str) -> NoneType

        Initialize this Email with recipients, subject and body.       """

        self.recipients = recipients
        self.subject = subject
        self.body = body

    def __str__(self):
        """ (Email) -> str

        Return a string representation of this email.
        """

        result = 'To: '
        for contact in self.recipients:
            result = result + '{0}, '.format(contact)

        result = result + '\nSubject: {0}'.format(self.subject)
        result = result + '\n{0}'.format(self.body)
        return result



class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType

        Initialize this Contact with first name first_name, last name
        last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address


    def __str__(self):
        """ (Contact) -> str

        Return a string representation of this contact.
        """
        return '{0} {1} <{2}>'.format(self.first_name,
            self.last_name, self.email_address)


    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """
        self.phone_number = telephone_num


class Author:
    def __init__(self, name):
        """ (______, str) -> NoneType """
        self.name = name


Q = 10

if Q == 1:
    # Select the code fragment(s) that create and initialize a Contact
    # using the constructor __init__).
    # A
    paul1 = Contact('Paul', 'Gries', 'paul@example.com')    # OK
    # B
    #contact = Contact()     # no-value-for-parameter
    #paul2 = Contact(contact, 'Paul', 'Gries', 'paul@example.com')
    # C
    #paul3 = Contact()       # no-value-for-parameter
    #paul3.first_name = 'Paul'
    #paul3.last_name = 'Gries'
    #paul3.email_address = 'paul@example.com'
    # D
    #info = ['Paul', 'Gries', 'paul@example.com']
    #paul4 = Contact(info)   # no-value-for-parameter
    print(paul1.email_address)

elif Q == 2:
    # This question uses class Contact from the previous question.
    # Variable jen refers to a Contact object. Select the correct way to print jen's email address.
    jen = Contact('Jen', 'Ny', 'jenny@example.com')
    # A
    #print(jen[2])
    # B
    #print(self.email_address)
    # C
    #print(jen.self.email_address)
    # D
    print(jen.email_address)         # OK

if Q == 3:
    # For a variable khaled that refers to a Contact object,
    # which code fragment correctly calls method add_phone_number?
    khaled = Contact('Khaled', 'Ali', 'khal@example.com')
    # A
    # khaled.add_phone_number(khaled, '555-1111')
    # B
    khaled.add_phone_number('555-1111')       # OK
    # C
    # khaled.add_phone_number() = '555-1111'
    # D
    # add_phone_number(khaled, '555-1111')
    print(khaled.phone_number)

if Q == 4:
    # This question uses class Contact from the previous questions,
    # and also uses types str, float, and list.

    # Here are several code fragments. In each fragment, there is a pair of method calls.
    # In some pairs, the two method calls are equivalent to each other,
    # and in the others, the two method calls are not equivalent to each other.
    # Select the code fragment(s) in which the method calls are equivalent to each other.

    # Assume that variable c refers to a Contact and that variable L refers to a list.
    c = Contact('Khaled', 'Ali', 'khal@example.com')
    L = [1, 2, 3, 4]
    # A
    a = str.replace('abc 123', '123', '246')     # OK
    b = 'abc 123'.replace('123', '246')
    assert a == b
    # B
    #a = L.index(3)
    #b = list.index(3)                           # TypeError
    # C
    c.add_phone_number('555-1111')               # OK
    a = c.phone_number
    Contact.add_phone_number(c, '555-1111')
    b = c.phone_number
    assert a == b
    # D
    #c.add_phone_number('555-1111')
    #c.add_phone_number(c1, '555-1111')          # NameError
    # E
    #a = (0.6).as_integer_ratio()
    #b = float.as_integer_ratio(float, 0.6)      # TypeError

elif Q == 5:
    # This question uses class Contact from the previous questions.

    # Variable rorik refers to a Contact object with instance variables first_name,
    # last_name and email_address that refer to 'Rorik', 'Henrikson'and 'rorik@example.com'
    # respectively.
    rorik = Contact('Rorik', 'Henrikson', 'rorik@example.com')
    # What is produced when str(rorik) is called?
    print(str(rorik))     # <__main__.Contact object at 0x000001975DD9BFD0>
    # A
    # 'Henrikson, Rorik <rorik@example.com>'
    # B
    # A string containing the types and memory addresses of the objects that first_name,
    # last_name, and email_address refer to.
    # C
    # A string containing information about the object that rorik refers to.     OK
    # This string contains both its type and its memory address.
    # D
    # 'Rorik Henrikson <rorik@example.com>'

elif Q == 6:
    # Variable rorik refers to a Contact object with instance variables first_name,
    # last_name and email_address that refer to 'Rorik', 'Henrikson'and 'rorik@example.com'
    # respectively.
    rorik = Contact('Rorik', 'Henrikson', 'rorik@example.com')
    # What is produced when str(rorik) is called?
    print(str(rorik))    # Rorik Henrikson <rorik@example.com>
    # A
    # 'Henrikson, Rorik <rorik@example.com>'
    # B
    # 'Rorik Henrikson <rorik@example.com>'           OK
    # C
    # A string containing the types and memory addresses of the objects that first_name,
    # last_name, and email_address refer to.
    # D
    # A string containing information about the object that rorik refers to.
    # This string contains both its type and its memory address.

elif Q == 7:
    # Which of the following can be used to create an Email object?
    # A
    #new_email = Email()                                       # no-value-for-parameter
    # B         OK
    new_email = Email([Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')], 'Hello', 'Hi there!\n Bye for now.')
    print(new_email)    # <__main__.Email object at 0x000002C6050BBE20>
    print(new_email.recipients, new_email.subject, new_email.body)
    # [<__main__.Contact object at 0x000002255EB1BFD0>] Hello Hi there! Bye for now.
    # C
    #new_email = Email('Hello', 'Hi there!\n Bye for now.')    # no-value-for-parameter
    # D
    student1 = Contact('Hugh', 'Z.', 'hugh@fakedomain.com')
    student2 = Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')
    student3 = Contact('Karin', 'Z.', 'karin@fakedomain.com')
    students = [student1, student2, student3]
    subject = 'LTP2: E4 is posted!'
    body = 'Hello,\nE4 is posted. Good luck!\n Paul and Jen'
    new_email = Email(students, subject, body)
    print(new_email.recipients, new_email.subject, new_email.body)

elif Q == 8:
    # Variable message refers to an Email object created with:
    recipients = [Contact('Paul', 'Gries', 'paul@example.com'), Contact('Jen', 'Campbell', 'jen@example.com')]
    subject = '2nd MOOC'
    body = 'Hi!\nI hope your 2nd MOOC is going well!\nBye :-)'
    message = Email(recipients, subject, body)
    # What is printed when print(message) is executed?
    print(message)
    #To: Paul Gries <paul@example.com>, Jen Campbell <jen@example.com>, 
    #Subject: 2nd MOOC
    #Hi!
    #I hope your 2nd MOOC is going well!
    #Bye :-)

elif Q == 9:
    # Which of the following is not a special method of object?
    # A: __lower__
    # B: __str__
    # C: __eq__
    # D: __ne__
    print(dir(object))
    # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    # '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
    # '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    # '__sizeof__', '__str__', '__subclasshook__']

elif Q == 10:
    # What should the blank (________) in the type contract be replaced with?
    # A: str
    # B: NoneType
    # C: Author                      OK
    # D: It is not possible to tell
    pass
