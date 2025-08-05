from sections import *

class MorningBriefTicket(Ticket):
    sections: [
        DateSection,
        TodoSection,
        BonusGoals,
        WhimsySection,
        ConcertSection,
    ]

