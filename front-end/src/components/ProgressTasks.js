import React from 'react';



const ProgressTasks = (props) => { 
    return (<div>
        <h1>IN PROGRESS</h1>
        <ul data-role="listview">
            {props.progressTasks}
        </ul>
    </div>);
}


export default ProgressTasks;