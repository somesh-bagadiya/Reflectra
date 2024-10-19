import reflex as pc


class JournalPage(pc.Component):
    def render(self):
        return pc.box(
            pc.text(
                "Daily Planner",
                font_size="2em",
                font_weight="bold",
                margin_bottom="1em",
            ),
            pc.vstack(
                pc.vstack(
                    pc.text(
                        "To-Do List",
                        font_size="1.5em",
                        font_weight="bold",
                        margin_bottom="0.5em",
                    ),
                    pc.text_area(
                        placeholder="Write your tasks here...",
                        width="100%",
                        height="200px",
                        padding="1em",
                        border_radius="8px",
                        border_color="gray.400",
                    ),
                    width="48%",
                    padding="1em",
                    bg="gray.50",
                    border_radius="10px",
                    box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
                ),
                pc.vstack(
                    pc.text(
                        "Notes",
                        font_size="1.5em",
                        font_weight="bold",
                        margin_bottom="0.5em",
                    ),
                    pc.text_area(
                        placeholder="Write your notes here...",
                        width="100%",
                        height="200px",
                        padding="1em",
                        border_radius="8px",
                        border_color="gray.400",
                    ),
                    width="48%",
                    padding="1em",
                    bg="gray.50",
                    border_radius="10px",
                    box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
                ),
                justify="space-between",
                width="100%",
                margin_bottom="1.5em",
            ),
            pc.vstack(
                pc.text(
                    "Daily Reflection",
                    font_size="1.5em",
                    font_weight="bold",
                    margin_bottom="0.5em",
                ),
                pc.text_area(
                    placeholder="Reflect on your day...",
                    width="100%",
                    height="150px",
                    padding="1em",
                    border_radius="8px",
                    border_color="gray.400",
                ),
                padding="1em",
                bg="gray.50",
                border_radius="10px",
                box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
            ),
            pc.button(
                "Save Entry",
                margin_top="2em",
                bg="teal.500",
                color="white",
                padding="0.8em 2em",
                border_radius="8px",
                _hover={"bg": "teal.600"},
            ),
            max_width="800px",
            margin="0 auto",
            padding="2em",
            bg="white",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
            border_radius="10px",
            margin_top="2em",
        )


def journalPage():
    return pc.flex(
        pc.box(
            pc.text(
                "Welcome to My Daily Planner",
                font_size="3em",
                font_weight="bold",
                margin="1em 0",
            ),
            text_align="center",
            margin_top="1em",
        ),
        JournalPage(),
        padding="5%",
        bg="gray.100",
        height="100vh",
        direction="column",
        align="center",
    )


# app = pc.App()
# app.add_page(index, title="My Daily Planner Page")
# app.compile()
