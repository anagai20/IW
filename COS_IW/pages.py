from dash import html
from navbar import create_navbar

# first page, lbw by race
def create_lbw_race_page():
   lbw_race = html.Div([
      html.H3('Low Birth Weight By Race',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('lbw_race.html','r').read(),width='100%',height='600')])
   layout = html.Div([
      create_navbar('Total'),
      lbw_race])
   
   return layout

# source of payment page

def payment_page():
   payment_total = html.Div([
      html.H3('Low Birth Weight by Source of Payment',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('payment_total.html','r').read(),width='100%',height='600')], 
      style = {'width':'50%','float':'left'})
   
   payment_race = html.Div([
      html.H3('Source of Payment by Race',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('payment_by_race.html','r').read(),width='100%',height='600')], 
      style = {'margin-left':'50%'})

   layout = html.Div([
      create_navbar('Source of Payment'),
      payment_total,
      payment_race])
   
   return layout

# weight gain page
def weight_gain_page():
   weight_gain_total = html.Div([
      html.H3('Low Birth Weight by Weight Gain of Mother', style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('weight_gain_total.html','r').read(),width='100%',height='600')], 
      style = {'width':'50%','float':'left'})
   
   weight_gain_race = html.Div([
      html.H3('Low Birth Weight by Weight Gain by Race',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('weight_gain_race.html','r').read(),width='100%',height='600')], 
      style = {'margin-left':'50%'})

   layout = html.Div([
      create_navbar('Mother\'s Weight Gain'),
      weight_gain_total,
      weight_gain_race])

   return layout

def prenatal_care_page():
   prenatal_total = html.Div([
      html.H3('Low Birth Weight by Number of Prenatal Visits', style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('prenatal_total.html','r').read(),width='100%',height='600')], 
      style = {'width':'50%','float':'left'})
   
   prenatal_race = html.Div([
      html.H3('Number of Prenatal Visits by Race',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('prenatal_race.html','r').read(),width='100%',height='600')], 
      style = {'margin-left':'50%'})
   hospitals = html.Div([
      html.H3('Distribution of Hospitals by Borough',style = {'color':'darkblue', 'text-align':'center'}),
      html.Iframe(id = 'map',srcDoc=open('hospitals.html','r').read(),width='100%',height='600')], 
      style = {'justify-content':'center'})
   layout = html.Div([
      create_navbar('Prenatal Care Visits'),
      prenatal_total,
      prenatal_race,
      hospitals])

   return layout