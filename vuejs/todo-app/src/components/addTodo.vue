<template>
  <div class="addTodo">
    <form class="addTodoForm">
        <label>Add a todo</label>
        <input class="field" type="text" v-model="newTodo.title" placeholder="Add a title">
        <input class="field" type="text" v-model="newTodo.content" placeholder="Add a description....">
        <button type="submit" @click.prevent="addTodo">+ Add</button>
    </form>
    <ListTodo 
        :todos="todos"
        @editTodo="editTodoByIndex"
    />
  </div>
</template>

<script>
import Todo from './Todo.vue'
import ListTodo from './ListTodo.vue'

export default {
    name: 'addTodo',
    components: {
        Todo,
        ListTodo
    },
    data() {
        return {
        newTodo: {
            title:'',
            content:''
        },
        todos: []
        }
    },
    methods: {
        addTodo(e) {
            console.log(this.newTodo);
            this.todos.push({
                id: this.todos.length + 1,
                title: this.newTodo.title,
                content: this.newTodo.content,
                completed: false
            })
            this.newTodo.title = '';
            this.newTodo.content = '';
        },
        editTodoByIndex(event){
            console.log(event);
            this.newTodo.title = event.title
            this.newTodo.content = event.content 
        }
    }
}
</script>

<style>
.addTodoForm {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
label {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}
.field {
    margin-bottom: 20px;
}
</style>