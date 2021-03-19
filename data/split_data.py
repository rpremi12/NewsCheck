import pandas as pd 
import math
main_df = pd.read_csv('metacriticuser_reviews.csv')

main_df['game'] = main_df.game.apply(lambda x: x if 'minecraft' not in x else 'minecraft')

game_counts = main_df.groupby(['platform', 'game'])


platform_counts = main_df.groupby('platform')['game'].count()

# print(platform_counts)



count_stratified = (game_counts['game'].count())

density_df = count_stratified/  platform_counts

# print(density_df)


# print(game_counts.get_group(('playstation-4', 'fortnite'))) # how to get value

unique_games = set(main_df.game)
# print(game_counts)
training = pd.DataFrame()
testing = pd.DataFrame()

test_per = .1
for game in unique_games:
	ps = game_counts.get_group(('playstation-4', game)) #['playstation-4'][game]#.get_group(('playstation-4', game))
	xbox = game_counts.get_group(('xbox-one', game))
	ps_count = ps.count()['game']
	xbox_count = xbox.count()['game']
	# print(ps.iloc[0:int(ps_count*(1-test_per)), :])
	# print(main_df.shape)

	training = pd.concat([training, ps.iloc[0:int(ps_count*(1-test_per)), :]])
	# print(ps_count)
	# print(training.groupby('platform').count())
	training = pd.concat([training, xbox.iloc[0:int(xbox_count*(1-test_per)), :]])
	# print(xbox_count)
	# print(training.groupby('platform').count())


	testing = pd.concat([testing, ps.iloc[int(ps_count*(1-test_per)):, :]])
	# print(testing.groupby('platform').count())
	testing = pd.concat([testing, xbox.iloc[int(xbox_count*(1-test_per)):, :]])

print(main_df.shape)
print(training.shape)
print(testing.shape)

training.to_csv('mc_training.csv')
testing.to_csv('mc_testing.csv')


