<template>
    <div class="listTodo">
        <div class="list-todo" v-for="(todo,index) in todos" :key="todo.id">
            <!-- remove is a custom event emitted by the child component called 'Todo' -->
                <Todo 
                    @remove="removeTodo(index)"
                    @edit="editTodo(index)" 
                    :todo="todo" 
                    :index="index"
                />
        </div>
    </div>
</template>

<script>
import Todo from './Todo.vue'
export default {
    name:'ListTodo',
    emits: ['editTodo'],
    components: {
        Todo
    },
    props: {
        todos: {
            type: Array,
            required: true
        }
    },
    methods: {
        removeTodo(index) {
            this.todos.splice(index, 1)
        },
        editTodo(index){
            console.log('form listtodo', index, this.todos[index]);
            this.$emit('editTodo', this.todos[index])
        }
    }
}
</script>

<style>

</style>