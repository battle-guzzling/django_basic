class SignUpRequestDto:
    def __init__(
        self,
        first_name,
        last_name,
        username,
        password,
        email,
        dob,
        phone_number,
        avatar,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.dob = dob
        self.phone_number = phone_number
        self.avatar = avatar
