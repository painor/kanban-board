import React from 'react';



class ProgressTask extends React.Component {
    constructor(props){
        super(props)
        this.state = {time:0}
        this.timer=setInterval( () => this.setState( (prevState)=> {return {time:prevState.time+1}} ),1000 );
    }
    render(){
        const e = this.props.taskname;
        let h = Math.floor(this.state.time / 3600);
        let m = Math.floor(this.state.time % 3600 / 60);
        let s = Math.floor(this.state.time % 3600 % 60);
        return (
        <li className="progress-task">
            <div>{e}</div>
        <span className="Timer">{h}:{m}:{s}</span>
            <button onClick={this.props.onResolve} className="Resolve-Button">Resolve</button>
        </li> 
    )
    }
    componentWillUnmount(){
        clearInterval(this.timer);
    }   
}
    

export default ProgressTask;