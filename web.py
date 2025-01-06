import streamlit as st
import helpers.todo_functions as tdf

st.title('My Todo App')
st.subheader('This is my todo app')

st.write('This app is to increase productivity')

todos = tdf.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    tdf.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        tdf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)

# st.session_state
