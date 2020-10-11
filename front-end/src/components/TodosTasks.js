import React from 'react';




const TodosTasks = (props) =>{
    
    return (<div>
    <h1 className="todo-title">TO DO</h1>
    <ul data-role="listview">
        {props.todoTasks}
        <li className="new-task">
            <button  onClick={ () =>{
                const name = prompt("Name Of the Task >");
                if (name) props.handler(name);
            } }>New Task</button>
        </li>
    </ul>
</div>)
}


export default TodosTasks;