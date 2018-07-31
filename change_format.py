i=1
with open ('G:/match_results/10_orb_match.txt','r') as file:
    lines = file.readlines()
file.close()

with open ('G:/match_results/10_orb_match.txt','w') as file:
    file.write(lines[0].rstrip('\n')+',')
    while i < len(lines):
      if i%4 !=0:
        file.write(lines[i].rstrip('\n')+',')
      else:
        file.write('\n'+lines[i].rstrip('\n')+',')
      i=i+1
file.close()