#tell it to start
import time
print("Welcome to Area 51 Adventure Game")
#ask for their name
name = raw_input("What is your name?")
#welcome them
while True:
	print("Alright, " + name + " you are stationed with 600,000 able-bodied soldiers outside Area 51.")
	#ask for a decision
	print("_____________________")
	first = raw_input("Will you airdrop in(type a) or use the back gate?(type b)")
	if first == "a":
		print("You have airdropped inside the top secret military base.")
		print("We need to make our message known that we are here.")
		second = raw_input("Will you deploy the Karens(a) or the Kyles(b)")
		if second == "a":
			print("_____________________")
			print("You have deployed the Karens and they have instinctively asked for the manager.")
			print("The manager has told the Head Karen to leave.")
			third = raw_input("Will you unleash the Kyles(a) or Naruto Run past the gaurds(b)")
			if third == "a":
				print("_____________________")
				print("The Kyles have all been obliterated by alien weapons. Ending 1.")
				break
			elif third == "b":
				print("_____________________")
				print("You have chosen to Naruto Run past the guards, making you faster than their bullets.")
				print("There are guards watching the Aliens holding cells. There's too many.")
				fourth = raw_input("Will you take out the guards on the left(a) or right(b)?")
				if fourth == "a":
					print("_____________________")
					print("The guards have seized most of your forces.")
					fifth = raw_input("Will you hit the big red button(a) or crash into the alien holding cell(b)?")
					if fifth == "a":
						print("_____________________")
						print("You have freed the aliens.")
						sixth = raw_input("Will you try to communicate with them(a) or lead them outside(b)?")
						if sixth == "a":
							print("_____________________")
							print("They were freaked out by your human language and killed everyone with their alien weapons.")
							print("Ending 2.")
							break
						elif sixth == "b":
							print("_____________________")
							print("The aliens are freed and are now your homies. Congrats You win.")
							print("Ending 3.")
							break							
					elif fifth == "b":
						print("_____________________")
						print("The holding cells are bound by an electrical forcefield")
						print("You have been electricuted. You lose")
						print("Ending 4.")
						break
				elif fourth == "b":
					print("_____________________")
					print("You have eliminated all of the guards, and hit the big red button.")
					print("The aliens have been freed.")
					fifth = raw_input("Will you try to commumicate with the aliens(a) or lead them outside(b)")	
					if fifth == "a":
						print("_____________________")
						print("They were freaked out by your human language and killed everyone with their alien weapons.")
						print("Ending 2.")
						break
					elif fifth == "b":
						print("_____________________")
						print("The aliens are freed and are now your homies. Congrats You win.")
						print("Ending 3.")
						break
		elif second == "b":
			print("_____________________")
			print("You have deployed the Kyles. They smashed the walls, causing thousands of dollars in damage.")
			print("You have been arrested for vandalism.")
			print("Ending 5.")
			break
	elif first == "b":
		print("_____________________")
		print("You have chosen to go through the back gate. Very sneaky.")
		second = raw_input("Will you send Chuck Norris(a) to do the job or the Rock(b)?")
		if second == "a":
			print("_____________________")
			print("Chuck Norris stared down the guards until they wet their pants.")
			print("The guards released all aliens in fear of what Chuck Norris would do to them.")
			print("You win. The aliens are now your homies.")
			print("Ending 6.")
			break
		elif second == "b":
			print("_____________________")
			print("The guards were distracted by what the Rock was cooking. They had a pleasant picnic.")
			print("You sneak in while the guards are eating hot dogs.")
			time.sleep(1)
			print("The head guard has approached you and told you to leave.")
			third = raw_input("Will you unleash the Kyles(a), Naruto Run in(b), or leave(c)?")
			if third == "c":
				print("_____________________")
				print("You tried to leave and the guards shot everybody. There were no survivors.")
				print("Ending 7.")
				break
			elif third == "a":
				print("_____________________")
				print("The Kyles have been obliterated by the guards. Everyone else was arrested for vandalism.")
				print("Ending 8.")
			elif third == "b":
				print("_____________________")
				print("You have Naruto Run in, dodging bullets because of your speed.")
				print("There is a red button and a blue button.")
				fourth = raw_input("You press the red button(a) or the blue button(b).")
				if fourth == "a":
					print("_____________________")
					print("The red button activates the nukes and everyone is blown into millions of pieces.")
					print("Ending 9.")
					break
				elif fourth == "b":
					print("_____________________")
					print("The blue button teleports you to an alien planet. You decide whether or not this is a win or loss.")
					print("Ending 10.")
					break	
		else:
			print("_____________________")
			print("That was an unrecognizable command, " + name + ". You should know better.")