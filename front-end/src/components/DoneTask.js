import React from 'react';



const DoneTask = (props) => {
    const e = props.taskname;
    return (
    <li>
        <div>{e}</div>
        <div className="price">{props.price}$</div>
    </li>
    )
}

export default DoneTask;
