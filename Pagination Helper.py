# Complete the PaginationHelper class, which is a utility class helpful for querying paging information
# related to an array.
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per
# each page. The types of values contained within the collection/array are not relevant.
# Handle errors with returning the integer -1 from the subunit, and optionally a print or log message explaining the
# nature of the error.
# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

# TODO: complete this class


# class PaginationHelper:
#
#
#     # The constructor takes in an array of items and a integer indicating
#
#     # how many items fit within a single page
#
#     def __init__(self, collection, items_per_page):
#
#         pass
#
#
#     # returns the number of items within the entire collection
#
#     def item_count(self):
#
#         pass
#
#
#     # returns the number of pages
#
#     def page_count(self):
#
#         pass
#
#
#     # returns the number of items on the current page. page_index is zero based
#
#     # this method should return -1 for page_index values that are out of range
#
#     def page_item_count(self, page_index):
#
#         pass
#
#
#     # determines what page an item is on. Zero based indexes.
#
#     # this method should return -1 for item_index values that are out of range
#
#     def page_index(self, item_index):
#
#         pass


class PaginationHelper:
    each_page = []
    number_of_pages = 0

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):

        if 0 < len(self.collection) / self.items_per_page <= 1:
            self.number_of_pages += 1
        elif len(self.collection) / self.items_per_page > 1:
            self.number_of_pages += int(len(self.collection) / self.items_per_page) + 1
        return self.number_of_pages

    def page_item_count(self, page_index):
        if -1 < page_index < self.number_of_pages:
            for i in range(len(self.collection)):
                if -1 < i < len(self.collection):
                    if i % self.items_per_page == 0 :
                        self.each_page.append(self.collection[i:i + self.items_per_page])

            return len(self.each_page[page_index])
            # return self.each_page
        else:
            return -1

    def page_index(self, item_index):
        if -1 < item_index < len(self.collection):
            for i in self.each_page:
                if self.collection[item_index] in i:
                    return self.each_page.index(i)
        else:
            return -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid
