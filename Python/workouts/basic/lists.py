colors=['red','green','yellow']

for i in range(len(colors)):
    print(len(colors))
    print(i)
    print(colors[i])
colors


process_completed=False
i=0
while not process_completed:
    print(' while loop at index:{}'.format(i))
    if process_completed:
        break
    else:
        i+=1
        if i==100:
            process_completed=True
            print('exiting while loop at index:{}'.format(i))

# lists & methods
si='append'
colors.append(si)
print(colors)
print()

colors.insert(2,'insert')
print(colors)

print(colors.index('yellow'))

