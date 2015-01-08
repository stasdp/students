# -*- coding: utf-8 -*-

class Paginator(object):
    def __init__(self, students, per_page):
        try:
            per_page = int(per_page)
        except ValueError:
            per_page = 10
        except TypeError:
            per_page = 10
        self.note_per_page = per_page
        self.count_of_notes = students.count()
        self.students = students
        self.current_number = 1
        self.num_pages
        self.page_range = []

    @property
    def num_pages(self):
        try:
            integer_page = self.count_of_notes / self.note_per_page
        except ZeroDivisionError:
            self.note_per_page = 10
            integer_page = self.count_of_notes / self.note_per_page
        if self.count_of_notes % self.note_per_page > 0:
            integer_page += 1
        return integer_page

    def page(self, number):
        try:
            number = int(number)
        except ValueError:
            number = 1
        except TypeError:
            number = 1
        self.current_number = number
        current_page = self.students[self.note_per_page*(number-1):self.note_per_page*number]
        current_page.has_previous = self.has_previous
        current_page.has_next = self.has_next
        current_page.number = self.current_number
        current_page.has_other_pages = self.has_other_pages
        current_page.next_page_number = self.next_page_number
        current_page.previous_page_number = self.previous_page_number
        current_page.count_notes = current_page.count()
        self.page_range = [x for x in range(1, self.num_pages + 1)]
        current_page.paginator = self
        return current_page

    @property
    def has_previous(self):
        return self.current_number > 1

    @property
    def has_next(self):
        return self.current_number < self.num_pages

    @property
    def has_other_pages(self):
        return self.num_pages > 0

    @property
    def next_page_number(self):
        if self.current_number < self.num_pages:
            return self.current_number + 1

    @property
    def previous_page_number(self):
        if self.current_number > 1:
            return self.current_number - 1
