from lecture_8.calender_app.Meeting import Meeting


class Calender:
    def __init__(self):
        self.meetings = []

    def creat_new_meeting(self, title, day, month, year, hour, minute, duration, reminder):
        meeting = Meeting(title, day, month, year, hour, minute, duration, reminder)
        self.meetings.append(meeting)

        return meeting

    def get_all_meeting_to_remind(self):
        res = []
        for m in self.meetings:
            if m.reminder:
                res.append(m)

        return res
