import { useState } from 'react';
import ApiCalendar from 'react-google-calendar-api';

function Calendar() {
    const [events, setEvents] = useState(null);

    const handleClick = (event) => {
        ApiCalendar.handleAuthClick()
            .then(() => {
                console.log('we\'re in')
            })
            .catch((error) =>
            console.log(error)
            )
    }

    const getEvents = () => {
        if (ApiCalendar.sign)
  ApiCalendar.listEvents({
      timeMin: new Date(Date.now()).toISOString(),
      timeMax: new Date(new Date().getTime()+(10*24*60*60*1000)).toISOString(),
      showDeleted: true,
      maxResults: 100,
      orderBy: 'updated'
  }).then(({ result }: any) => {
    console.log(result.items);
    setEvents(result.items)
  });
    }

    return (
        <div>
            <button
                onClick={(event) =>
                    handleClick(event)
                }
            >AUTH GOOGLE</button>
            <button
                onClick={() => {
                    getEvents() 
                }}>get 10 Events
            </button>
            <button
                onClick={() => {
                  console.log(events[1].recurrence[0].match(/(BYDAY=)([A-Z,*]{1,7})/g))
                }}>log today
            </button>
        </div>
    )
};

export default Calendar;