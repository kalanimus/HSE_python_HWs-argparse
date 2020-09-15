import argparse

G = ['male', 'female']
H = ['No', 'Yes', '3_years', 'Yes,but_no_doctor']
M = ['Good', 'Neutral', 'Bad']
HA = ['Week', 'Month', 'Year']

parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')
parser.add_argument('--Name')
parser.add_argument('--Gender', choices=G)
parser.add_argument('Height', type=int)
parser.add_argument('Weight', type=int)
parser.add_argument('Sleep_hours', type=int)
parser.add_argument('Meals', type=int)
parser.add_argument('Fruits', type=int)
parser.add_argument('Steps', type=int)
parser.add_argument('Monitoring_health', choices=H)
parser.add_argument('Mood', choices=M)
parser.add_argument('Happiness', choices=HA)

args = parser.parse_args()

p = 0

if args.Sleep_hours == 7 or args.Sleep_hours == 8:
    p += 1
if args.Meals >= 4:
    p += 1
if args.Steps > 10000:
    p += 1
if args.Fruits > 500:
    p += 1
if args.Monitoring_health == H[2]:
    p += 1
if args.Mood == M[0]:
    p += 1
if args.Happiness == HA[0] or args.Happiness == HA[1]:
    p += 1

He = args.Height / 100
BMI = args.Weight / (He ** 2)

if 18.5 < BMI < 24.9:
    p += 1

if 5 <= p <= 7:
    print('Your score is', p, 'You are on the right track!')
elif p < 5:
    print('Your score is', p, 'You need to rethink your healthy lifestyle!')
else:
    print('Your score is', p, 'You are a true leader in a healthy lifestyle!')

