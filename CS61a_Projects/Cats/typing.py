"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
	"""Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
	paragraph returns true. If there are fewer than K such paragraphs, return
	the empty string.
	"""
	# BEGIN PROBLEM 1 

	'''For some reason the for loop and range won't work properly for me'''



	j = 0

	x = 0

	for i in paragraphs:

		if select(i):

			if k == j:

				return paragraphs[x]

			else:

				j+=1

		x += 1

	return ""
	# END PROBLEM 1


def about(topic):
	"""Return a select function that returns whether a paragraph contains one
	of the words in TOPIC.

	>>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
	>>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
	'Cute Dog!'
	>>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
	'Nice pup.'
	"""
	assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
	# BEGIN PROBLEM 2

	'''def select(x):    	

		j = ''

		for i in x:

			j += lower(i)

		for k in range(len(topic)):

			word = topic[k - 1]

			if word in j:

				return True

		return False

	return select'''

	def about_helper (str):
		str_array = split(remove_punctuation(lower(str)))
		for x in range (len(str_array)):
			for i in range (len(topic)):
				if (topic[i] == str_array[x]):
					return True
		return False
	return about_helper

	'''elif topic_count < total_topic - 1: 

				topic_count += 1

				return select(topic[topic_count]) 	

			else:

				return False'''
	# END PROBLEM 2


def accuracy(typed, reference):
	"""Return the accuracy (percentage of words typed correctly) of TYPED
	when compared to the prefix of REFERENCE that was typed.

	>>> accuracy('Cute Dog!', 'Cute Dog.')
	50.0
	>>> accuracy('A Cute Dog!', 'Cute Dog.')
	0.0
	>>> accuracy('cute Dog.', 'Cute Dog.')
	50.0
	>>> accuracy('Cute Dog. I say!', 'Cute Dog.')
	50.0
	>>> accuracy('Cute', 'Cute Dog.')
	100.0
	>>> accuracy('', 'Cute Dog.')
	0.0
	"""
	typed_words = split(typed)
	reference_words = split(reference)

	# BEGIN PROBLEM 3
	'''count = 0

	if typed == '':

		return float(0)

	for i in range(len(typed_words) - 1):

		if typed_words[i] == reference_words[i]:

			count += 1

	return float(100 *(count / len(typed_words)))'''
	if (len(typed_words)==0):
		return 0.0
	correct=0
	if len(typed_words) > len(reference_words): #check if the length of the typed array is longer than the reference array
		for i in range (len(typed_words)-len(reference_words)):
			reference_words += [""] #since typed array is longer, add extra EMPTY slots into reference array so they match
	for x in range (len(typed_words)):
		if typed_words[x]==reference_words[x]: #comparing each element in the two arrays
			correct +=1
	return correct/(len(typed_words))*100
	# END PROBLEM 3


def wpm(typed, elapsed):
	"""Return the words-per-minute (WPM) of the TYPED string."""
	assert elapsed > 0, 'Elapsed time must be positive'

	# BEGIN PROBLEM 4
	char_counter = 0

	for x in typed:

		char_counter += 1

	new = char_counter / 5

	return ((new * 60) / elapsed)
	# END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
	"""Returns the element of VALID_WORDS that has the smallest difference
	from USER_WORD. Instead returns USER_WORD if that difference is greater
	than or equal to LIMIT.
	"""
	# BEGIN PROBLEM 5
	'''if user_word in valid_words:

		return user_word

	k, l = 0, 0

	for i in valid_words:

		if max(diff_function(user_word, valid_words[k], limit), diff_function(user_word, valid_words[l +1], limit)) == valid_words[k]:

			k, l = k + 1, l + 1

		else:

			l += 1

	if diff_function(user_word, valid_words[k], limit) < limit:

		return valid_words[k]

	else:

		return user_word'''

	prev = 1000 #arbitrary high starting unit - the first return of diff_function will always be lower and hence will assigned to prev
	for x in range (0,len(valid_words)):
		if valid_words[x] == user_word:
			return user_word
		else:
			new=diff_function(user_word,valid_words[x],limit)
			if new<prev:
				index = x
				prev = new
	if (diff_function(user_word,valid_words[index],limit)>limit):
		return user_word
	return valid_words[index]



	'''def lowest_diff(user_word, valid_words, valid_word_count, diff_function, limit):

		lowest = valid_words[valid_word_count]

		next_lowest = diff_function(user_word, valid_words[valid_word_count + 1], limit)

		if min(lowest, next_lowest) == lowest:

			return lowest_diff(user_word, valid_words, valid_word_count, diff_function, limit)

		else:

			return lowest_diff(user_word, valid_words + 1, valid_word_count, diff_function, limit)'''


	# END PROBLEM 5


def swap_diff(start, goal, limit):
	"""A diff function for autocorrect that determines how many letters
	in START need to be substituted to create GOAL, then adds the difference in
	their lengths.
	"""
	# BEGIN PROBLEM 6

	if limit == 0 and start != goal:
		return 1
	elif limit == 0 and start == goal:
		return 0
	elif len(start)==0:
		return len(goal)
	elif len(goal)==0:
		return len(start)
	elif start[0]!=goal[0]:
		return 1 + swap_diff(start[1:],goal[1:],limit-1)
	else:
		return swap_diff(start[1:],goal[1:],limit)
	# END PROBLEM 6

def edit_diff(start, goal, limit):
	"""A diff function that computes the edit distance from START to GOAL."""
	#print("start:", start)
	#print("goal:", goal)

	if start == goal and limit == 0:

		return 0

	elif start != goal and limit == 0:

		return 1

	elif goal == "" and start == "":

		return 0

	elif goal == "" and start != "":

		return 1 + edit_diff(start[1:], goal, limit - 1)

	elif start == "" and goal != "":

		return 1 + edit_diff((goal[0] + start), goal, limit -1)

	elif start[0] == goal[0]: # Fill in the condition
		# BEGIN
		return edit_diff(start[1:], goal[1:], limit)
		# END

	else:
		#print("entered edit")
		add_diff = 1 + edit_diff((goal[0] + start), goal, limit -1) # Fill in these lines
		remove_diff = 1 + edit_diff(start[1:], goal, limit - 1)
		substitute_diff = 1 + edit_diff(goal[0] + start[1:], goal, limit -1)
		# BEGIN
		return min(add_diff, remove_diff, substitute_diff)

		# END


def final_diff(start, goal, limit):
	"""A diff function. If you implement this function, it will be used."""
	assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
	"""Send a report of your id and progress so far to the multiplayer server."""
	# BEGIN PROBLEM 8

	count, final = 0, 0

	for i in range(len(typed)):

		if typed[i] != prompt[i] or i == len(typed):

			final = float(count + 1 / len(prompt))

		else:

			count += 1

	send({"id":id, "progress":final})

	return final

	# END PROBLEM 8


def fastest_words_report(word_times):
	"""Return a text description of the fastest words typed by each player."""
	fastest = fastest_words(word_times)
	report = ''
	for i in range(len(fastest)):
		words = ','.join(fastest[i])
		report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
	return report


def fastest_words(word_times, margin=1e-5):
	"""A list of which words each player typed fastest."""
	n_players = len(word_times)
	n_words = len(word_times[0]) - 1
	assert all(len(times) == n_words + 1 for times in word_times)
	assert margin > 0
	# BEGIN PROBLEM 9

	j = []
	for n in range(n_words):

		for x in range(n_words):

			get_low = elapsed_time(word_times[n][x+1]) - elapsed_time(word_times[n][x])

			for b in range(n_words):

				k,  = []



				get_other_low = elapsed_time(word_times[n+1][x+1]) - elapsed_time(word_times[n+1][x])

				if get_other_low < get_low:



					k += [word(word_times[0][1])]

		j += k


		


	# END PROBLEM 9


def word_time(word, elapsed_time):
	"""A data abstrction for the elapsed time that a player finished a word."""
	return [word, elapsed_time]


def word(word_time):
	"""An accessor function for the word of a word_time."""
	return word_time[0]


def elapsed_time(word_time):
	"""An accessor function for the elapsed time of a word_time."""
	return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
	"""Measure typing speed and accuracy on the command line."""
	paragraphs = lines_from_file('data/sample_paragraphs.txt')
	select = lambda p: True
	if topics:
		select = about(topics)
	i = 0
	while True:
		reference = choose(paragraphs, select, i)
		if not reference:
			print('No more paragraphs about', topics, 'are available.')
			return
		print('Type the following paragraph and then press enter/return.')
		print('If you only type part of it, you will be scored only on that part.\n')
		print(reference)
		print()

		start = datetime.now()
		typed = input()
		if not typed:
			print('Goodbye.')
			return
		print()

		elapsed = (datetime.now() - start).total_seconds()
		print("Nice work!")
		print('Words per minute:', wpm(typed, elapsed))
		print('Accuracy:        ', accuracy(typed, reference))

		print('\nPress enter/return for the next paragraph or type q to quit.')
		if input().strip() == 'q':
			return
		i += 1


@main
def run(*args):
	"""Read in the command-line argument and calls corresponding functions."""
	import argparse
	parser = argparse.ArgumentParser(description="Typing Test")
	parser.add_argument('topic', help="Topic word", nargs='*')
	parser.add_argument('-t', help="Run typing test", action='store_true')

	args = parser.parse_args()
	if args.t:
		run_typing_test(args.topic)