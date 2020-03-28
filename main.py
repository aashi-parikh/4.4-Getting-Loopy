def draw_8():
	my_string = ''
	for i in range(8):
		my_string += '* '
	my_string = my_string[0:15]
	output_string =''
	
	for j in range(8):
		output_string += my_string + "\n"
	return output_string[0:127]

print(draw_8())
print(len(draw_8()))

def stars_and_stripes():
	star_row = ''
	dash_row = ''
	combined_string = ''
	output_string = ''
	for i in range(7):
		star_row += '* '
	for j in range(7):
		dash_row += '- '
	star_row = star_row[0:13]
	dash_row = dash_row[0:13]
	combined_string = combined_string + star_row + '\n' + dash_row
	for k in range(3):
		output_string += '\n' + combined_string
	return output_string[1:84]
	
print(stars_and_stripes())
print(len(stars_and_stripes()))

def vertical_stars_and_stripes():
	row = ''
	output = ''
	for i in range(3):
		row += '- * '
	for j in range(6):
		output += "\n" + row + '-'
	return output[1:84]

print(vertical_stars_and_stripes())
print(len(vertical_stars_and_stripes()))


def increasing_triangle(x):
	f=''
	o = ''
	for i in range(x): 
		o=''
		for j in range(0, i+1): 
			o += str(j+1) + ' '
		o = o[0:(len(o)-1)]
		f += o + "\n"
	return f[0:(len(f)-1)]
print(increasing_triangle(7))
		