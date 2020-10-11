import React from 'react';

const DoneTasks = (props) => {
    return <div>
        <h1>DONE</h1>
        <ul data-role="listview">
            {props.doneTasks}
        </ul>
    </div>
}


export default DoneTasks