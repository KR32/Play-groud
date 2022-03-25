<template>
    <div class="todo">
       <h1>{{ todo.title }}
        <button @click="sendTodoIndexToParentComponentToRemove">X</button>
        <button @click="sendTodoIndexToParentComponentToEdit">.../</button>
        </h1>
       <p>{{ todo.content }}</p>
       <span>{{ todo.completed }}</span>
    </div>
</template>

<script>
export default {
    name: 'Todo',    
    emits: ['remove', 'edit'], 
    props: {
        todo : {
                id: 1,
                title: '',
                content: '',
                completed: false
            }
    },
    methods: {
        sendTodoIndexToParentComponentToRemove() {
            console.log('from sendTodoIndexToParentComponentToRemove', this.todo);
            // remove is an custom event that is emitted by Todo component
            // and it is listened by the parent component called ListTodo
            // ListtTodo is having the method removeTodo which is called while the event 'remove' is emitted
            // form here we are passing the index of the todo as event payload to the parent component while emitting the event
            this.$emit('remove')
        },
        sendTodoIndexToParentComponentToEdit(){
            console.log('from sendTodoIndexToParentComponentToEdit', this.todo);
            this.$emit('edit')
        }
    },

}
</script>

<style>

</style>