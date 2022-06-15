from oAuth import OAuth
import datetime

account = OAuth()
schedule = account.schedule()

now_time = datetime.datetime.now()
end_time = datetime.timedelta(days=30)
range_time = (now_time + end_time).strftime('%Y-%m-%d')

q = schedule.new_query('start').greater_equal(now_time)
q.chain('and').on_attribute('end').less_equal(range_time)

getSchedule = schedule.get_events(query=q, include_recurring=True)
for event in getSchedule:
    print(event)
    print('')
