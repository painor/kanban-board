import React from 'react';
import { render } from 'react-dom';
import TodosTasks from './components/TodosTasks'
import TodoTask from './components/TodoTask'
import ProgressTasks from './components/ProgressTasks'
import ProgressTask from './components/ProgressTask'
import DoneTasks from './components/DoneTasks';
import DoneTask from './components/DoneTask'

const base_url = "https://jx2ubbcvfi.execute-api.us-east-1.amazonaws.com/dev/";

function makeid(length) {
    var result = "";
    var characters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            todo: [],
            progress: [],
            done: []
        };
        this.addNewTask = this.addNewTask.bind(this);
        this.handlerStart = this.handlerStart.bind(this);
        this.onResolve = this.onResolve.bind(this);
    }

    async addNewTask(name) {
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "task_title": name
            })
        };

        const response = await fetch(base_url + "new_task", settings);
        const result = await response.json();
        if (result.success) {
            this.setState((prevState) => {
                return {todo: prevState.todo.concat(<TodoTask handlerStart={() => this.handlerStart(result.task.id)} key={result.task.id} taskname={name}/>)};
            })
        } else {
            alert("Error happened " + result.error);
        }
    }

    async onResolve(key) {
        const progress = this.state.progress;
        const selected = progress.filter((e) => {
            return e.key == key;
        })[0];
        console.log(selected);
        const new_progress = progress.filter((e) => {
            return e.key != key;
        });
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "task_id": Number(key)
            })
        };

        const response = await fetch(base_url + "resolve_task", settings);
        const result = await response.json();
        if (!result.success) {
            alert("Error happened " + result.error);
            return;
        }
        this.setState((prevState) => {
            return {
                progress: new_progress,
                done: prevState.done.concat(<DoneTask key={key} price={result.task.price} taskname={selected.props.taskname}/>)
            };
        })

    }

    async handlerStart(key) {
        const tasks = this.state.todo;
        const selected = tasks.filter((e) => {
            return e.key == key;
        })[0];
        console.log(selected);
        const new_todo = tasks.filter((e) => {
            return e.key != key;
        });
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "task_id": Number(key)
            })
        };

        const response = await fetch(base_url + "start_task", settings);
        const result = await response.json();
        if (!result.success) {
            alert("Error happened " + result.error);
            return;
        }
        this.setState((prevState) => {
            return {
                todo: new_todo,
                progress: prevState.progress.concat(
                    <ProgressTask key={key}
                                  onResolve={() => this.onResolve(key)}
                                  taskname={selected.props.taskname}/>
                )
            };
        })


    }

    render() {
        return (
            <div className="row">
                <div className="col-sm">
                    <TodosTasks handler={this.addNewTask} todoTasks={this.state.todo}/>
                </div>
                <div className="col-sm">
                    <ProgressTasks progressTasks={this.state.progress}/>
                </div>
                <div className="col-sm">
                    <DoneTasks doneTasks={this.state.done}/>
                </div>
            </div>
        )
    }
}


render(<App/>, document.getElementById("container"));
