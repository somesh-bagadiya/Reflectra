import reflex as rx
from rxconfig import config
import datetime
import uuid
import asyncio


def generate_id():
    return str(uuid.uuid4())


class Task(rx.Model, table=True):
    uuid: str
    date: str
    task: str


def add_task_to_db(uid, date, task):
    with rx.session() as session:
        session.add(
            Task(
                uuid=uid,
                date=date,
                task=task,
            )
        )
        session.commit()


class State(rx.State):
    """The app state."""

    task: str = ""
    task_list: list[list]
    on_delete: str = "translate (-20px, 0px)"
    off_delete: str = "translate (0px, 0px)"
    on_opacity_delete: str = "100%"
    off_opacity_delete: str = "0%"

    def update_task_field(self, task: list):
        self.task = task

    async def delete_task(self, task: list):
        print("inside delete", task)
        uuid = task[0]
        self.task_list = [
            [uid, date, task, delete_pos_x, delete_opacity]
            for uid, date, task, delete_pos_x, delete_opacity in self.task_list
            if uid != uuid
            ]

    async def show_delete(self, task: list):
        print(task)
        uuid = task[0]
        self.task_list = [
            (
                [uid, date, task, self.on_delete, self.on_opacity_delete]
                if uid == uuid
                else [uid, date, task, delete_pos_x, delete_opacity]
            )
            for uid, date, task, delete_pos_x, delete_opacity in self.task_list
        ]

        await asyncio.sleep(0.05)

    async def hide_delete(self, task):
        uuid = task[0]
        self.task_list = [
            (
                [uid, date, task, self.off_delete, self.off_opacity_delete]
                if uid == uuid
                else [uid, date, task, delete_pos_x, delete_opacity]
            )
            for uid, date, task, delete_pos_x, delete_opacity in self.task_list
        ]
        await asyncio.sleep(0.05)

    async def add_task_to_list(self):
        print("here:", self.task)
        uid = generate_id()
        self.task_list.append(
            [
                uid,
                datetime.datetime.now().strftime("%B %d, %U %H:%M"),
                self.task,
                self.off_delete,
                self.off_opacity_delete,
            ]
        )

        # add_task_to_db(
        #     uid,
        #     datetime.datetime.now().strftime("%B %d, %U %H:%M"),
        #     self.task,
        # )
        self.task = ""

    def delete_all(self):
        self.task_list = []

    ...


def create_delete_button(transform, opacity, delete_func) -> rx.Component:
    return rx.container(
        rx.button(
            rx.icon(tag="trash", color="red"),
            width="50px",
            height="50px",
            color_scheme=None,
        ),
        justify_content="right",
        on_click=delete_func
        # transform=transform,
        # opacity=opacity,
        # transition="transform 0.65s, opacity 0.55s ease",
    )


def display_task(task) -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.container(
                rx.vstack(
                    rx.container(
                        rx.text(
                            task[1],  # the date
                            font_size="8px",
                            font_weight="bold",
                            color="#374151",
                        )
                    ),
                    rx.container(
                        rx.text(
                            task[2],  # the task
                            font_size="14px",
                            font_weight="bold",
                            color="#374151",
                        )
                    ),
                    spacing="1px",
                ),
                padding="0px",
            ),
            create_delete_button(task[3], task[4], State.delete_task(task)),
            width="100%",
        ),
        width="100%",
        height="60px",
        border_bottom="1px solid #9xa3af",
        padding="0px",
        border_radius="0px",
        display="flex",
        justify="space-between",
        align_items="center",
        overflow="hidden",
        # on_mouse_over=State.show_delete(State.task)
        # on_mouse_leave=State.hide_delete(State.task)
    )


def task_input_field() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.container(
                rx.text(
                    "Full stack to-do app",
                    font_size="24px",
                    font_weight="900",
                    color="#4b79a1",
                ),
            ),
            rx.spacer(),
            rx.hstack(
                rx.input(
                    value=State.task,
                    border="None",
                    width="300px",
                    height="45px",
                    border_bottom="1px solid black",
                    border_radius="0px",
                    focus_border_color="None",
                    on_change=State.update_task_field,
                ),
                rx.button(
                    rx.icon(
                        tag="arrow_right",
                        color="black",
                        font_size="14px",
                    ),
                    width="45px",
                    height="45px",
                    color_scheme=None,
                    padding_top="1%",
                    border_radius="0px",
                    border_bottom="1px solid black",
                    on_click=State.add_task_to_list,
                ),
                rx.button(
                    rx.icon(
                        tag="trash",
                        color="black",
                        font_size="14px",
                    ),
                    width="45px",
                    height="45px",
                    color_scheme=None,
                    padding_top="1%",
                    border_radius="0px",
                    border_bottom="1px solid black",
                    on_click=State.delete_all,
                ),
                spacing="0px",
            ),
        ),
    )


def todoListPage() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.container(task_input_field()),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.container(
                rx.vstack(
                    rx.foreach(State.task_list, display_task),
                    width="400px",
                    height="500px",
                    overflow="hidden",
                ),
                height="500px",
                overflow="hidden",
                border_radius="10px",
                padding_top="5%",
                padding_bottom="5%",
                box_shadow="7px -7px 14px #cccecf, -7px 7px 14px #ffffff",
            ),
        ),
        background="#ebedee",
        max_width="auto",
        height="100vh",
        display="grid",
        place_items="center",
    )
