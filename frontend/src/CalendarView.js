import Kalend, { CalendarView } from 'kalend' // import component
import 'kalend/dist/styles/index.css'; // import styles

function CAL({viewEvents}) {
    return(
        <div  style={{
            height: '60vh'
          }}>
    <Kalend
    //   onEventClick={onEventClick}
    //   onNewEventClick={onNewEventClick}
    events={
        viewEvents
    }
    initialDate={new Date().toISOString()}
       hourHeight={30}
      initialView={CalendarView.WEEK}
       disabledViews={[CalendarView.DAY, CalendarView.MONTH, CalendarView.THREE_DAYS, CalendarView.AGENDA]}
       timeFormat={'12'}
      weekDayStart={'Monday'}
      disableMobileDropdown={true}
    />
    </div>
    )
}
    export default CAL;