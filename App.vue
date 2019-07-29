<template lang="pug">
#app
  .ui.action.input
    input(type="text", v-model="todo", @keydown.enter="addTask()")
    button.ui.icon.button(@click="addTask()")
      i.plus.icon
  
  .ui.checkbox(v-for="task in tasks")
    .task(@click="toggleTask(task)")
      input(type="checkbox", v-model="task.done")
      label(v-if="task.done")
        del {{ task.title }}
      label(v-else) {{ task.title }}
      .icon
        i.list.icon(@click.stop="showDetails(task)")
        i.close.icon(@click.stop="deleteTask(task)", v-if="task.done")
    task-details(v-show="task.detail", :item="task")
    .ui.divider
</template>


<script>
  export default{

    components: {
      'task-details': require('./TaskDetails.vue').default,
    },

    data(){
      return{
        todo: "abc",
        tasks: [],
          // {
          //   title: tsk,
          //   done: false,
          //   detail: false,
          //   content: "",
          //   date: "",
          // }
      }
    },

    methods: {
      addTask: function(){
        var tsk = this.todo;
        if(tsk){
          this.tasks.push({
            title: tsk,
            done: false,
            detail: false,
            content: "",
            date: "",
          });
          this.todo = "";
        }
      },
      deleteTask: function(tsk){
        this.tasks.splice(this.tasks.indexOf(tsk), 1);
      },
      showDetails: function(tsk){
        tsk.detail = !tsk.detail;
      },
      toggleTask: function(tsk){
        tsk.done = !tsk.done;
      }
    },

  }
</script>


<style lang="sass">
  #app
    display: flex
    flex-direction: column 
    margin: auto
    width: 20em
    padding: 2vw

  .task
    margin: 1.5vw 0
    display: flex
    justify-content: space-between
    font-size: 16px
</style>
