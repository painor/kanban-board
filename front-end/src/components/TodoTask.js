import React from 'react';

const TodoTask = (props) =>{
    const e = props.taskname;
    return(
    <li>
        <div>
            {e}
        </div>
        <button onClick={props.handlerStart} className="Start-Button">Start</button>
    </li> 
    );
    
}

export default TodoTask;