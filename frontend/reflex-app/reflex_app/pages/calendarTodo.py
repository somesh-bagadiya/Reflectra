import reflex as rx

def create_icon(icon_name):
    """Create an icon with specified dimensions and display properties."""
    return rx.icon(
        tag=icon_name,
        height="1.25rem",
        display="inline-block",
        width="1.25rem",
    )


def create_icon_button(icon_name):
    """Create a button with an icon and specific styling properties."""
    return rx.el.button(
        create_icon(icon_name=icon_name),
        background_color="#374151",
        _hover={"background-color": "#6B7280"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#E5E7EB",
    )


def create_heading(font_size, line_height, text):
    """Create a heading with custom font properties and styling."""
    return rx.heading(
        text,
        font_weight="700",
        margin_bottom="1rem",
        color="#F3F4F6",
        font_size=font_size,
        line_height=line_height,
        as_="h2",
    )


def create_bold_text(text):
    """Create a bold text element with specific color."""
    return rx.box(text, font_weight="600", color="#D1D5DB")


def create_bordered_text(text):
    """Create a bordered text element with specific padding and styling."""
    return rx.box(
        create_bold_text(text=text),
        border_bottom_width="1px",
        border_color="#374151",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_colored_box(bg_color, text_color, content):
    """Create a colored box with custom background, text color, and content."""
    return rx.box(
        content,
        background_color=bg_color,
        margin_top="0.25rem",
        padding="0.25rem",
        border_radius="0.25rem",
        color=text_color,
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_bordered_colored_box(
    title, bg_color, text_color, content
):
    """Create a bordered box with a title and colored content area."""
    return rx.box(
        create_bold_text(text=title),
        create_colored_box(
            bg_color=bg_color,
            text_color=text_color,
            content=content,
        ),
        border_bottom_width="1px",
        border_color="#374151",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_checkbox():
    """Create a styled checkbox input element."""
    return rx.el.input(
        type="checkbox",
        background_color="#374151",
        border_color="#4B5563",
        margin_right="0.5rem",
    )


def create_text_span(text):
    """Create a text span with specific color styling."""
    return rx.text.span(text, color="#D1D5DB")


def create_checkbox_list_item(text):
    """Create a list item with a checkbox and text."""
    return rx.el.li(
        create_checkbox(),
        create_text_span(text=text),
        display="flex",
        align_items="center",
    )


def create_date_navigation():
    """Create a date navigation component with today button and direction controls."""
    return rx.flex(
        rx.el.button(
            "Today",
            background_color="#4F46E5",
            _hover={"background-color": "#4338CA"},
            padding_left="1rem",
            padding_right="1rem",
            padding_top="0.5rem",
            padding_bottom="0.5rem",
            border_radius="0.5rem",
            color="#ffffff",
        ),
        create_icon_button(icon_name="chevron-left"),
        create_icon_button(icon_name="chevron-right"),
        display="flex",
        column_gap="0.5rem",
    )


def create_calendar_header():
    """Create a calendar header with title and date navigation."""
    return rx.flex(
        rx.heading(
            "Calendar",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#F3F4F6",
            as_="h1",
        ),
        create_date_navigation(),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_bottom="1.5rem",
    )


def create_daily_schedule():
    """Create a daily schedule grid with time slots and events."""
    return rx.box(
        create_bordered_text(text="8:00 AM"),
        create_bordered_colored_box(
            title="9:00 AM",
            bg_color="#312E81",
            text_color="#C7D2FE",
            content="Team Meeting",
        ),
        create_bordered_text(text="10:00 AM"),
        create_bordered_text(text="11:00 AM"),
        create_bordered_colored_box(
            title="12:00 PM",
            bg_color="#064E3B",
            text_color="#A7F3D0",
            content="Lunch Break",
        ),
        create_bordered_text(text="1:00 PM"),
        create_bordered_colored_box(
            title="2:00 PM",
            bg_color="#78350F",
            text_color="#FDE68A",
            content="Client Call",
        ),
        create_bordered_text(text="3:00 PM"),
        create_bordered_text(text="4:00 PM"),
        create_bordered_colored_box(
            title="5:00 PM",
            bg_color="#7F1D1D",
            text_color="#FECACA",
            content="Project Deadline",
        ),
        gap="0.5rem",
        display="grid",
        grid_template_columns="repeat(1, minmax(0, 1fr))",
    )


def create_task_input():
    """Create an input field for adding new tasks."""
    return rx.el.input(
        class_name="placeholder-gray-400",
        placeholder="Add new task",
        type="text",
        background_color="#374151",
        border_width="1px",
        border_color="#4B5563",
        padding="0.5rem",
        border_radius="0.25rem",
        color="#F3F4F6",
        width="100%",
    )


def create_add_task_button():
    """Create a button for adding new tasks."""
    return rx.el.button(
        "Add Task",
        background_color="#4F46E5",
        _hover={"background-color": "#4338CA"},
        margin_top="0.5rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#ffffff",
        width="100%",
    )


def create_todo_list():
    """Create a todo list component with tasks and input for new tasks."""
    return rx.box(
        create_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            text="Todo List",
        ),
        rx.list(
            create_checkbox_list_item(
                text="Prepare presentation"
            ),
            create_checkbox_list_item(
                text="Review project timeline"
            ),
            create_checkbox_list_item(
                text="Send follow-up emails"
            ),
            create_checkbox_list_item(
                text="Update team on progress"
            ),
            create_checkbox_list_item(
                text="Schedule next week's meetings"
            ),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        rx.box(
            create_task_input(),
            create_add_task_button(),
            margin_top="1rem",
        ),
        background_color="#1F2937",
        padding="1rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        width="33.333333%",
    )


def create_calendar_and_todo():
    """Create a combined view of calendar and todo list."""
    return rx.flex(
        rx.box(
            create_heading(
                font_size="1.5rem",
                line_height="2rem",
                text="June 1, 2023",
            ),
            create_daily_schedule(),
            background_color="#1F2937",
            flex_grow="1",
            padding="1rem",
            border_radius="0.5rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        ),
        create_todo_list(),
        display="flex",
        gap="1rem",
    )


def create_main_container():
    """Create the main container for the entire application layout."""
    return rx.box(
        rx.box(
            create_calendar_header(),
            create_calendar_and_todo(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding="1rem",
        ),
        background_color="#111827",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        color="#F3F4F6",
    )


def create_app_layout():
    """Create the complete application layout including styles and content."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_main_container(),
    )