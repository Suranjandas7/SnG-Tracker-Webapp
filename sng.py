#Suranjan Das Poker SnG Tracker
import csv

class SnG(object):
	def __init__(self, config):
		self.config = config
		self.history = []
		self.T_matches = self.config[0]
		self.Name = 'Suranjan Das'
		self.in_stake = self.config[1]
		self.out_stake = self.config[2]
		self.Played = self.config[3]
		self.Won = self.config[4]
		self.Lost = self.config[5]
		
	def return_stats(self):
		GLTP = float(int(self.T_matches) - int(self.Played))
		c = round(100 - (GLTP/float(self.T_matches)*100),2)
		win_per = round(float((float(self.Won)/float(self.Played)) * 100),2)
		cash_won = int(self.out_stake)*int(self.Won)
		cash_lost = int(self.in_stake)*int(self.Lost)
		net_cash = cash_won - cash_lost
		projected_winnings = int(GLTP*(win_per/100)) * int(self.out_stake)  
		projected_loses = (int(GLTP) - int(GLTP*(win_per/100))) * int(self.in_stake)
		projected_net = projected_winnings - projected_loses
		worst_ECP = -int(GLTP * int(self.in_stake)) + net_cash
		best_ECP = int(GLTP * int(self.out_stake)) + net_cash
		final_data = [] #Name##P-W-L##CW-CL##WR##PN##AWPO

		#0,1,2,3,4,5,6,7 -> Name, PWL, CW-CL, NC, WP, PN, EWP,WECP
		final_data.append(str(self.Name))
		final_data.append(str(self.Played) + '-' + str(self.Won) + '-' + str(self.Lost))
		final_data.append(str(cash_won) + '-' + str(cash_lost))
		final_data.append(str(net_cash))
		final_data.append(str(win_per)) 
		final_data.append(str(projected_net))
		final_data.append(str(int(net_cash) + int(projected_net)))
		final_data.append(str(worst_ECP))
		final_data.append(str(best_ECP))

		h = '''<html>
				<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
				<body>
				<div class="jumbotron text-center"><h1>SnG Tracker v0.2</h1><p>{data}</p></div>
				<table class = "table">
				<thead><tr><th>Particulars</th><th>Details</th></tr></thead>
		'''.format(data = final_data[0])

		m1 = '<tr><td>P-W-L</td><td>{data}</td></tr>'.format(data = final_data[1])
		m2 = '<tr><td>Cash Won-Lost</td><td>{data}</td></tr>'.format(data = final_data[2])
		m3 = '<tr><td>Net Cash</td><td>{data}</td></tr>'.format(data = final_data[3])
		m4 = '<tr><td></td><td></td>'
		m5 = '<tr><td>Win Percentage</td><td>{data}</td></td>'.format(data = final_data[4])
		m6 = '<tr><td>Projected Net</td><td>{data}</td></td>'.format(data = final_data[5])
		m4 = '<tr><td></td><td></td>'
		m8 = '<tr><td><b>W-ECP</b></td><td><b>{data}</b></td></td>'.format(data = final_data[7])
		m7 = '<tr><td><b>ECP</b></td><td><b>{data}</b></td></td>'.format(data = final_data[6])
		m9 = '<tr><td><b>W-ECP</b></td><td><b>{data}</b></td></td>'.format(data = final_data[8])

		f = '''
				</table>
				</bpdy>
			    </html>
		'''.format(data = final_data[0])
		b = str(h)+str(m1)+str(m2)+str(m3)+str(m4)+str(m5)+str(m6)+str(m4)+str(m8)+str(m7)+str(m9)+str(f)
		
		return b