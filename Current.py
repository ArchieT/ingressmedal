# -*- coding: utf-8 -*-

class Current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactiveliness, currorg, argdod):
		from interactive import Interactive

		self.current = {}
		self.current.update(currorg)

		interaktywnosc = Interactive()
		self.interaktywnosc = interaktywnosc
		if interactiveliness == False:
			for kluczykoa in interaktywnosc.GivMeCurQSdict().keys():
				try:
					bzdurkaldkfh = str(currorg[kluczykoa])
					if bzdurkaldkfh is None or bzdurkaldkfh == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()
				except:
					print "Interactively is False. There is no %s, exiting." % kluczykoa
					quit()
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				try:
					bzdurkafdhgljsdk = str(currorg[kluczykoa])
					if bzdurkafdhgljsdk is None or bzdurkafdhgljsdk == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()

				except:
					print "Interactively is False. There is no %s, exiting. Next time put in at least an 'n' character." % kluczykoa
					quit()
		elif interactiveliness == True:
			kluczykoal = []
			# print interaktywnosc.GivMeCurQSdict().keys() #debug
			# print interaktywnosc.GivMeCurQUSdict().keys() #debug
			for kluczykoa in interaktywnosc.GivMeCurQSdict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkaldkfh = str(currorg[kluczykoa])
					# print "jesttraj" #debug
					# print bzdurkaldkfh #debug
					# print "----------------" #debug
					if bzdurkaldkfh is None or bzdurkaldkfh == "None" or not (type(int(bzdurkaldkfh)) == int):
						print type(bzdurkaldkfh)
						kluczykoal.append(str(kluczykoa))
					# print "jestnolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "niema" #debug
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkafdhgljsdk = str(currorg[kluczykoa])
					# print "jestTrajProba" #debug
					# print bzdurkafdhgljsdk #debug
					# print "--------" #debug
					if bzdurkafdhgljsdk is None or bzdurkafdhgljsdk == "None" or self.CzyLiczbaZeroDoPiecDziewiatekLUBn(
							bzdurkafdhgljsdk) == False:
						kluczykoal.append(str(kluczykoa))
					# print "jestNolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "NiMa" #debug
			# kluczbejs = (interaktywnosc.GivMeCurQSdict().keys() + interaktywnosc.GivMeCurQUSdict().keys()).sort()
			kluczbejs = []
			kluczbejs.extend(interaktywnosc.GivMeCurQSdict().keys())
			kluczbejs.extend(interaktywnosc.GivMeCurQUSdict().keys())
			# print kluczbejs  # debug
			kluczbejs.sort()
			# print kluczbejs  # debug
			kluczykoal.sort()
			# print "kluczbejs" #debug
			# print kluczbejs #debug
			# print "kluczvs" #debug
			# print kluczvs #debug
			# print "kluczykoal" #debug
			# print kluczykoal  # debug
			if kluczbejs == kluczykoal:
				current = interaktywnosc.currentraz()
				self.current.update(current)
			else:
				# if True:
				try:
					current = {}
					for kluczykob in kluczykoal:
						current[kluczykob] = interaktywnosc.currentwyrywki(kluczykob)
					# print current[kluczykob]
					self.current.update(current)
				except:
					pass
		else:
			print "Interactively can't be: "
			try:
				print interactiveliness
			except:
				print "<unreadable>"
			print "   because such value is unsuitable for the situation."
			print "Exiting"
			quit()
		self.codename = codename

	def rjeturncount(self):
		return self.current

	@staticmethod
	def TrueczyFalse(ciag):
		if ((str(ciag == "True")) or (ciag == "y") or (ciag == "yes")) or (
						(ciag == "False") or (ciag == "n") or (ciag == "no")):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatek(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatekLUBn(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or (str(ciag) == 'n'):
			return True
		else:
			return False

	@property
	def coUNTINGcurapcountable(self):
		current = self.current
		curapcountable = {'seer': int((int(current['seer']) * 1000)),
						  'depllater': int((int((current['depl']) - int(current['capt'])) * 65)),
						  'link': int((int(current['link']) * 313)), 'field': int((int(current['field']) * 1250)),
						  'rechmin': int(((int(current['rech']) / 1000) * 10)),
						  'captres': int((int(current['capt']) * 625)), 'destr': int((int(current['destr']) * 75)),
						  'destrlink': int((int(current['destrlink']) * 187)),
						  'destrfield': int((int(current['destrfield']) * 750))}
		self.namesforcurapcountable = {'seer': "Portals discovered (submitted)",
									   'depllater': "Sure points from deployment of resonators except the capturing one and from upgrading resonators",
									   'link': "Links created", 'field': "Control Fields created",
									   'rechmin': "Minimum AP gained on recharging",
									   'captres': "Capturing portals + first resonator",
									   'destr': "Destroyed resonators", 'destrlink': "Enemy links destroyed",
									   'destrfield': "Enemy Control Fields destroyed",
									   'photo': "Photos added to portals", 'edit': "Edits done to portals' data"}
		if current['photo'] == 'n':
			print "That's your fault you don't know how much AP you've gained on photos."
		else:
			curapcountable['photo'] = (current['photo'] * 500)
		if current['edit'] == 'n':
			print "That's your fault you don't know how much AP you've gained on edits."
		else:
			curapcountable['edit'] = (current['edit'] * 200)
		return curapcountable

	def percentofap(self):
		things = self.coUNTINGcurapcountable
		descripts = self.namesforcurapcountable
		percenty = {}
		tabelka = []
		left = self.current['ap']
		for w in sorted(things, key=things.get, reverse=True):
			percenty[w] = str("{:.4%}".format((float(things[w])) / (float(self.current['ap']))))
			left -= things[w]
			tabelka.append([descripts[w], things[w], percenty[w]])
		tabelka.append(["Uncomputable", left, str("{:.4%}".format((float(left)) / (float(self.current['ap']))))])
		print "Total AP: %s" % str(self.current['ap'])
		from tabulate import tabulate
		print tabulate(tabelka, headers=["Description", "AP", "Percent of total AP"])

	def percentofdest(self):
		import tabulate

		def minapfromact(name, value, apable):
			if apable == True:
				if name == 'seer':
					pass
				elif name == 'depl':
					pass
				elif name == 'link':
					pass
				elif name == 'field':
					pass
				elif name == 'rech':
					pass
				elif name == 'capt':
					pass
				elif name == 'uniqcapt':
					pass
				elif name == 'destr':
					pass
			else:
				return False

		current = self.current
		things = self.coUNTINGcurapcountable
		ap = current['ap']
		self.lvldict = {
			1: {'ap': 0, 'bene': {'itemy': True, 'xm': 3000, 'rd': 250, 'gamebegun': True}},
			2: {'ap': 2500, 'bene': {'itemy': True, 'xm': 4000, 'rd': 500, 'gamebegun': False}},
			3: {'ap': 20000, 'bene': {'itemy': True, 'xm': 5000, 'rd': 750, 'gamebegun': False}},
			4: {'ap': 70000, 'bene': {'itemy': True, 'xm': 6000, 'rd': 1000, 'gamebegun': False}},
			5: {'ap': 150000, 'bene': {'itemy': True, 'xm': 7000, 'rd': 1250, 'gamebegun': False}},
			6: {'ap': 300000, 'bene': {'itemy': True, 'xm': 8000, 'rd': 1500, 'gamebegun': False}},
			7: {'ap': 600000, 'bene': {'itemy': True, 'xm': 9000, 'rd': 1750, 'gamebegun': False}},
			8: {'ap': 1200000, 'bene': {'itemy': True, 'xm': 10000, 'rd': 2000, 'gamebegun': False}},
			9: {'ap': 2400000, 'silver': 4, 'gold': 1, 'bene': {'itemy': False, 'xm': 10900, 'rd': 2250, 'gamebegun': False}},
			10: {'ap': 4000000, 'silver': 5, 'gold': 2, 'bene': {'itemy': False, 'xm': 11700, 'rd': 2500, 'gamebegun': False}},
			11: {'ap': 6000000, 'silver': 6, 'gold': 5, 'bene': {'itemy': False, 'xm': 12400, 'rd': 2750, 'gamebegun': False}},
			12: {'ap': 8400000, 'silver': 7, 'gold': 6, 'bene': {'itemy': False, 'xm': 13000, 'rd': 3000, 'gamebegun': False}},
			13: {'ap': 12000000, 'gold': 7, 'platinum': 1, 'bene': {'itemy': False, 'xm': 13500, 'rd': 3250, 'gamebegun': False}},
			14: {'ap': 17000000, 'platinum': 2, 'bene': {'itemy': False, 'xm': 13900, 'rd': 3500, 'gamebegun': False}},
			15: {'ap': 24000000, 'platinum': 3, 'bene': {'itemy': False, 'xm': 14200, 'rd': 3750, 'gamebegun': False}},
			16: {'ap': 40000000, 'platinum': 4, 'onyx': 2, 'bene': {'itemy': False, 'xm': 14400, 'rd': 4000, 'gamebegun': False}},
		}
		self.medaldict = {
			'uniqvis': {'name': 'Explorer', 'apable' = False, 'walk': {'bronze': 100, 'silver': 1000, 'gold': 2000, 'platinum': 10000, 'onyx': 30000}, 'over': 'False', 'sub': 'False'},
			'seer': {'name': 'Seer', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'hack': {'name': 'Hacker', 'apable' = False, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'depl': {'name': 'Builder', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'link': {'name': 'Connector', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'field': {'name': 'Mind Controller', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'rech': {'name': 'Recharger', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'capt': {'name': 'Liberator', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'uniqcapt': {'name': 'Pioneer', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'destr': {'name': 'Purifier', 'apable' = True, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
			'guard': {'name': 'Guardian', 'apable' = False, 'walk': {'bronze': , 'silver': , 'gold': , 'platinum': , 'onyx': }, 'over': 'False', 'sub': 'False'},
		}
