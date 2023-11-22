CREATE TABLE USERS (
    user_id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    given_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    profile_description TEXT NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE CAREGIVER (
    caregiver_user_id INTEGER PRIMARY KEY REFERENCES USERS(user_id) ON DELETE CASCADE,
    photo VARCHAR(255) NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')) NOT NULL,
    caregiving_type TEXT CHECK (caregiving_type IN ('babysitter', 'caregiver for elderly', 'playmate for children')) NOT NULL,
    hourly_rate DECIMAL(8, 2) NOT NULL
);

CREATE TABLE MEMBER (
    member_user_id INTEGER PRIMARY KEY REFERENCES USERS(user_id) ON DELETE CASCADE,
    house_rules TEXT NOT NULL
);

CREATE TABLE ADDRESS (
    member_user_id INTEGER PRIMARY KEY REFERENCES MEMBER(member_user_id) ON DELETE CASCADE,
    house_number VARCHAR(10) NOT NULL,
    street VARCHAR(100) NOT NULL,
    town VARCHAR(50) NOT NULL
);


CREATE TABLE JOB (
    job_id INTEGER PRIMARY KEY,
    member_user_id INTEGER NOT NULL,
    required_caregiving_type TEXT CHECK (required_caregiving_type IN ('babysitter', 'caregiver for elderly', 'playmate for children')) NOT NULL,
    other_requirements TEXT,
    date_posted DATE NOT NULL,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id) ON DELETE CASCADE
);

CREATE TABLE JOB_APPLICATION (
    caregiver_user_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    date_applied DATE NOT NULL,
    PRIMARY KEY (caregiver_user_id, job_id),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES JOB(job_id) ON DELETE CASCADE
);

CREATE TABLE APPOINTMENT (
    appointment_id INTEGER PRIMARY KEY,
    caregiver_user_id INTEGER NOT NULL,
    member_user_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL  ,
    work_hours INTEGER NOT NULL,
    status TEXT CHECK (status IN ('accepted', 'declined', 'pending')) NOT NULL,
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id) ON DELETE CASCADE
);


-- Insert data into USER table
INSERT INTO USERS (email, given_name, surname, city, phone_number, profile_description, password)
VALUES
	('caregiver1@example.com', 'Karim', 'Kazakov', 'Astana', '+77771000001', 'Responsible with elderly.', 'password'),
	('caregiver2@example.com', 'Marat', 'Maratov', 'Astana', '+77771000002', 'Experienced caregiver for elderly.', 'password'),
    ('caregiver3@example.com', 'Askar', 'Askarov', 'Almaty', '+77771000003', 'Professional babysitter with CPR certification.', 'password'),
    ('caregiver4@example.com', 'Dina', 'Doszhanova', 'Astana', '+77771000004', 'Friendly playmate for children.', 'password'),
    ('caregiver5@example.com', 'Elena', 'Ermakova', 'Almaty', '+77771000005', 'Experienced caregiver for elderly.', 'password'),
    ('caregiver6@example.com', 'Farida', 'Fazilova', 'Astana', '+77771000006', 'Responsible and caring babysitter.', 'password'),
    ('caregiver7@example.com', 'Gani', 'Ganiev', 'Almaty', '+77771000007', 'Elderly care specialist with medical background.', 'password'),
    ('caregiver8@example.com', 'Helen', 'Harrison', 'Astana', '+77771000008', 'Fun and creative playmate for children.', 'password'),
    ('caregiver9@example.com', 'Ivan', 'Ivanov', 'Almaty', '+77771000009', 'Experienced caregiver for elderly.', 'password'),
    ('caregiver10@example.com', 'Julia', 'Jones', 'Astana', '+77771000010', 'Certified babysitter with first aid training.', 'password'),

    ('member1@example.com', 'Bolat', 'Bolatov', 'Almaty', '+77771000011', 'Family of four looking for a reliable babysitter.', 'password'),
    ('member2@example.com', 'Laura', 'Lopez', 'Astana', '+77771000012', 'Elderly couple in need of a caring caregiver.', 'password'),
    ('member3@example.com', 'Mikhail', 'Mironov', 'Almaty', '+77771000013', 'Single parent seeking a trustworthy babysitter.', 'password'),
    ('member4@example.com', 'Natalia', 'Nazarova', 'Astana', '+77771000014', 'Family with no pets looking for elderly care.', 'password'),
    ('member5@example.com', 'Oscar', 'Olivares', 'Almaty', '+77771000015', 'Parents of two energetic kids looking for a playful babysitter.', 'password'),
    ('member6@example.com', 'Pavel', 'Petrov', 'Astana', '+77771000016', 'Elderly woman seeking a compassionate caregiver.', 'password'),
    ('member7@example.com', 'Qing', 'Qiu', 'Almaty', '+77771000017', 'Family with strict house rules looking for a babysitter.', 'password'),
    ('member8@example.com', 'Rita', 'Rodriguez', 'Astana', '+77771000018', 'Couple looking for a responsible caregiver for their elderly parents.', 'password'),
    ('member9@example.com', 'Sergei', 'Sokolov', 'Almaty', '+77771000019', 'Single parent seeking a reliable babysitter for regular evenings.', 'password'),
    ('member10@example.com', 'Tatiana', 'Tolstaya', 'Astana', '+77771000020', 'Family with no pets looking for elderly care.', 'password');

-- Insert data into CAREGIVER table
INSERT INTO CAREGIVER (caregiver_user_id, photo, gender, caregiving_type, hourly_rate)
VALUES
	(1, 'https://example.com/caregiver1/photo.jpg', 'Male', 'babysitter', 7.00),
    (2, 'https://example.com/caregiver2/photo.jpg', 'Female', 'caregiver for elderly', 15.00),
    (3, 'https://example.com/caregiver3/photo.jpg', 'Male', 'playmate for children', 6.00),
    (4, 'https://example.com/caregiver4/photo.jpg', 'Female', 'caregiver for elderly', 11.50),
    (5, 'https://example.com/caregiver5/photo.jpg', 'Male', 'babysitter', 5.00),
	(6, 'https://example.com/caregiver6/photo.jpg', 'Female', 'caregiver for elderly', 21.00),
    (7, 'https://example.com/caregiver7/photo.jpg', 'Other', 'playmate for children', 8.00),
    (8, 'https://example.com/caregiver8/photo.jpg', 'Male', 'caregiver for elderly', 10.00),
    (9, 'https://example.com/caregiver9/photo.jpg', 'Female', 'babysitter', 12.50),
    (10, 'https://example.com/caregiver10/photo.jpg', 'Other', 'playmate for children', 14.00);


-- Insert data into MEMBER table
INSERT INTO MEMBER (member_user_id, house_rules)
VALUES
	(11, 'Keep the house tidy'),
	(12, 'No shoes inside, quiet hours after 9 PM'),
    (13, 'No pets.'),
	(14, 'No pets, keep the house tidy'),
	(15, 'Quiet household, no loud music'),
    (16, 'Family with strict house rules, looking for a caregiver who respects them.'),
    (17, 'No pets.'),
    (18, 'Elderly couple looking for a caregiver with medical background.'),
    (19, 'Large family seeking a fun and responsible babysitter for occasional evenings.'),
    (20, 'No pets.');

-- Insert data into ADDRESS table
INSERT INTO ADDRESS (member_user_id, house_number, street, town)
VALUES
	(11, '158', 'Qabanbay street', 'Almaty'),
	(12, '456', 'Turan street', 'Astana'),
	(13, '547', 'Makar street', 'Almaty'),
	(14, '123', 'Turan street', 'Astana'),
	(15, '456', 'Qabanbay street', 'Almaty'),
	(16, '789', 'Tauelsiz street', 'Astana'),
	(17, '213', 'Turanid street', 'Almaty'),
	(18, '215', 'Muchalik street', 'Astana'),
	(19, '217', 'Teremen street', 'Almaty'),
	(20, '313', 'Tauelsiz street', 'Astana');
	
-- Insert data into JOB table
INSERT INTO JOB (member_user_id, required_caregiving_type, other_requirements, date_posted)
VALUES
	(11, 'babysitter', 'gentle, responsible', '2023-11-04'),
	(15, 'caregiver for elderly', 'can cook, assist with toilet, responsible', '2023-11-04'),
	(15, 'caregiver for elderly', 'can lift up to 25 kg', '2023-11-14'),
	(14, 'babysitter', 'gentle, responsible, can cook', '2023-11-16'),
	(17, 'playmate for children', 'knows children games, gentle', '2023-11-16'),
	(11, 'babysitter', 'responsible', '2023-11-17'),
	(18, 'caregiver for elderly', 'can cook, assist with toilet, responsible', '2023-11-18'),
	(16, 'caregiver for elderly', 'gentle, can lift up to 10 kg', '2023-11-19'),
	(13, 'babysitter', 'responsible, can cook', '2023-11-19'),
	(12, 'playmate for children', 'knows children games, gentle', '2023-11-22'),
	(14, 'babysitter', 'gentle, responsible, caring', '2023-11-22');
	

-- Insert data into JOB_APPLICATION table
INSERT INTO JOB_APPLICATION (caregiver_user_id, job_id, date_applied)
VALUES
    (3, 2, '2023-11-04'),
    (7, 2, '2023-11-04'),
    (1, 1, '2023-11-05'),
	(6, 3, '2023-11-05'),
	(2, 4, '2023-11-16'),
	(5, 5, '2023-11-16'),
	(8, 6, '2023-11-17'),
	(10, 7, '2023-11-18'),
	(4, 8, '2023-11-19'),
	(9, 9, '2023-11-19'),
	(3, 10, '2023-11-22');

-- Insert data into APPOINTMENT table
INSERT INTO APPOINTMENT (caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status)
VALUES
    (7, 15, '2023-11-06', '12:00', 4, 'declined'),
    (3, 15, '2023-11-06', '12:00', 4, 'accepted'),
	(1, 11, '2023-11-07', '15:00', 3, 'accepted'),
	(6, 15, '2023-11-08', '10:00', 5, 'accepted'),
	(2, 14, '2023-11-16', '14:00', 6, 'declined'),
	(5, 17, '2023-11-17', '16:00', 2, 'pending'),
	(8, 18, '2023-11-18', '13:00', 4, 'declined'),
	(8, 16, '2023-11-19', '11:00', 6, 'accepted'),
	(4, 13, '2023-11-19', '09:00', 8, 'pending'),
	(9, 12, '2023-11-22', '17:00', 3, 'pending');