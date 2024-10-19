import reflex as rx

def create_icon(icon_tag):
    """Create an icon with specified tag and styling."""
    return rx.icon(
        tag=icon_tag,
        height="1.25rem",
        display="inline-block",
        width="1.25rem",
    )


def create_icon_button(button_icon_tag):
    """Create a styled button with an icon."""
    return rx.el.button(
        create_icon(icon_tag=button_icon_tag),
        background_color="#E5E7EB",
        _hover={"background-color": "#D1D5DB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#374151",
    )


def create_option(option_text):
    """Create a select option element with given text."""
    return rx.el.option(option_text)


def create_header_cell(cell_content):
    """Create a styled header cell for the calendar."""
    return rx.box(
        cell_content,
        font_weight="600",
        padding="0.5rem",
        text_align="center",
        color="#4B5563",
    )


def create_muted_text(text_content):
    """Create a box with muted text color."""
    return rx.box(text_content, color="#9CA3AF")


def create_calendar_day_cell(day_number):
    """Create a calendar day cell with muted text."""
    return rx.box(
        create_muted_text(text_content=day_number),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        border_right_width="1px",
        height="8rem",
        padding="0.5rem",
    )


def create_bold_text(text_content):
    """Create a box with bold text."""
    return rx.box(text_content, font_weight="700")


def create_event_label(bg_color, text_color, label_text):
    """Create a styled event label for the calendar."""
    return rx.box(
        label_text,
        background_color=bg_color,
        margin_top="0.25rem",
        padding="0.25rem",
        border_radius="0.25rem",
        color=text_color,
        font_size="0.75rem",
        line_height="1rem",
    )


def create_calendar_day_with_event(
    day_number, event_bg_color, event_text_color, event_text
):
    """Create a calendar day cell with an event."""
    return rx.box(
        create_bold_text(text_content=day_number),
        create_event_label(
            bg_color=event_bg_color,
            text_color=event_text_color,
            label_text=event_text,
        ),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        border_right_width="1px",
        height="8rem",
        padding="0.5rem",
    )


def create_calendar_day(day_number):
    """Create a standard calendar day cell."""
    return rx.box(
        create_bold_text(text_content=day_number),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        border_right_width="1px",
        height="8rem",
        padding="0.5rem",
    )


def create_next_month_day(day_number):
    """Create a calendar day cell for the next month."""
    return rx.box(
        create_muted_text(text_content=day_number),
        border_color="#E5E7EB",
        border_right_width="1px",
        height="8rem",
        padding="0.5rem",
    )


def create_colored_icon(icon_color, icon_tag):
    """Create a colored icon with specified tag."""
    return rx.icon(
        tag=icon_tag,
        height="1.25rem",
        margin_right="0.5rem",
        color=icon_color,
        width="1.25rem",
    )


def create_event_text(event_description):
    """Create styled text for an event description."""
    return rx.text.span(event_description, color="#374151")


def create_event_list_item(
    icon_color, icon_tag, event_text
):
    """Create a list item for an event with an icon and description."""
    return rx.el.li(
        create_colored_icon(
            icon_color=icon_color, icon_tag=icon_tag
        ),
        create_event_text(event_description=event_text),
        display="flex",
        align_items="center",
    )


def create_view_selector():
    """Create a select element for choosing calendar view (Month/Week/Day)."""
    return rx.el.select(
        create_option(option_text="Month"),
        create_option(option_text="Week"),
        create_option(option_text="Day"),
        background_color="#ffffff",
        border_width="1px",
        border_color="#D1D5DB",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
    )


def create_calendar_controls():
    """Create the control panel for the calendar, including navigation and view selection."""
    return rx.flex(
        rx.el.button(
            "Today",
            background_color="#3B82F6",
            _hover={"background-color": "#2563EB"},
            padding_left="1rem",
            padding_right="1rem",
            padding_top="0.5rem",
            padding_bottom="0.5rem",
            border_radius="0.5rem",
            color="#ffffff",
        ),
        create_icon_button(button_icon_tag="chevron-left"),
        create_icon_button(button_icon_tag="chevron-right"),
        create_view_selector(),
        display="flex",
        column_gap="0.5rem",
    )


def create_calendar_header():
    """Create the header for the calendar, including title and controls."""
    return rx.flex(
        rx.heading(
            "Calendar",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#1F2937",
            as_="h1",
        ),
        create_calendar_controls(),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_bottom="1.5rem",
    )


def create_weekday_header():
    """Create the header row with weekday names for the calendar."""
    return rx.box(
        create_header_cell(cell_content="Sun"),
        create_header_cell(cell_content="Mon"),
        create_header_cell(cell_content="Tue"),
        create_header_cell(cell_content="Wed"),
        create_header_cell(cell_content="Thu"),
        create_header_cell(cell_content="Fri"),
        create_header_cell(cell_content="Sat"),
        border_bottom_width="1px",
        border_color="#E5E7EB",
        gap="1px",
        display="grid",
        grid_template_columns="repeat(7, minmax(0, 1fr))",
    )


def create_calendar_grid():
    """Create the main calendar grid with day cells and events."""
    return rx.box(
        create_calendar_day_cell(day_number="30"),
        create_calendar_day_cell(day_number="31"),
        create_calendar_day_with_event(
            day_number="1",
            event_bg_color="#DBEAFE",
            event_text_color="#1E40AF",
            event_text="9:00 AM Meeting",
        ),
        create_calendar_day(day_number="2"),
        create_calendar_day_with_event(
            day_number="3",
            event_bg_color="#D1FAE5",
            event_text_color="#065F46",
            event_text="2:00 PM Call",
        ),
        create_calendar_day(day_number="4"),
        rx.box(
            create_bold_text(text_content="5"),
            border_bottom_width="1px",
            border_color="#E5E7EB",
            height="8rem",
            padding="0.5rem",
        ),
        create_calendar_day(day_number="6"),
        create_calendar_day_with_event(
            day_number="7",
            event_bg_color="#FEF3C7",
            event_text_color="#92400E",
            event_text="11:00 AM Presentation",
        ),
        create_calendar_day(day_number="8"),
        create_calendar_day(day_number="9"),
        create_calendar_day(day_number="10"),
        create_calendar_day_with_event(
            day_number="11",
            event_bg_color="#FEE2E2",
            event_text_color="#991B1B",
            event_text="3:00 PM Deadline",
        ),
        create_calendar_day(day_number="12"),
        create_calendar_day(day_number="13"),
        create_calendar_day(day_number="14"),
        create_calendar_day(day_number="15"),
        create_calendar_day(day_number="16"),
        create_calendar_day(day_number="17"),
        create_calendar_day(day_number="18"),
        create_calendar_day(day_number="19"),
        create_calendar_day(day_number="20"),
        create_calendar_day(day_number="21"),
        create_calendar_day(day_number="22"),
        create_calendar_day(day_number="23"),
        create_calendar_day(day_number="24"),
        create_calendar_day(day_number="25"),
        create_calendar_day(day_number="26"),
        create_calendar_day(day_number="27"),
        create_calendar_day(day_number="28"),
        create_calendar_day(day_number="29"),
        create_calendar_day(day_number="30"),
        create_calendar_day(day_number="31"),
        create_next_month_day(day_number="1"),
        create_next_month_day(day_number="2"),
        gap="1px",
        display="grid",
        grid_template_columns="repeat(7, minmax(0, 1fr))",
    )


def create_upcoming_events():
    """Create a box with a list of upcoming events."""
    return rx.box(
        rx.heading(
            "Upcoming Events",
            font_weight="700",
            margin_bottom="1rem",
            font_size="1.25rem",
            line_height="1.75rem",
            as_="h2",
        ),
        rx.list(
            create_event_list_item(
                icon_color="#3B82F6",
                icon_tag="calendar",
                event_text="9:00 AM Meeting - Today",
            ),
            create_event_list_item(
                icon_color="#10B981",
                icon_tag="phone",
                event_text="2:00 PM Call - Jun 3",
            ),
            create_event_list_item(
                icon_color="#F59E0B",
                icon_tag="presentation",
                event_text="11:00 AM Presentation - Jun 7",
            ),
            create_event_list_item(
                icon_color="#EF4444",
                icon_tag="clock",
                event_text="3:00 PM Deadline - Jun 11",
            ),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        background_color="#ffffff",
        margin_top="1.5rem",
        padding="1rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )


def create_calendar_layout():
    """Create the overall layout for the calendar, including header, grid, and upcoming events."""
    return rx.box(
        create_calendar_header(),
        rx.box(
            create_weekday_header(),
            create_calendar_grid(),
            background_color="#ffffff",
            border_radius="0.5rem",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        ),
        create_upcoming_events(),
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
    )


def create_calendar_page():
    """Create the complete calendar page, including styles and layout."""
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
        rx.box(
            create_calendar_layout(),
            background_color="#F3F4F6",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )
