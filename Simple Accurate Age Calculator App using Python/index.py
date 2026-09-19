"""
MASA Accurate Age & Chronology Analytics
Developer: MASA
"""

from datetime import date, datetime
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaAgeCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MASA Age Analytics")
        self.geometry("460x520")
        self.resizable(False, False)
        self.configure(fg_color="#0F172A")

        self._build_ui()

    def _build_ui(self):
        header_card = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=14)
        header_card.pack(fill="x", padx=20, pady=(20, 15))

        title = ctk.CTkLabel(
            header_card,
            text="MASA AGE ANALYTICS",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#38BDF8",
        )
        title.pack(pady=(12, 2))

        subtitle = ctk.CTkLabel(
            header_card,
            text="High-Precision Chronological Lifespan Calculator",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 12))

        inputs_card = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=14)
        inputs_card.pack(fill="x", padx=20, pady=5)

        for col in range(3):
            inputs_card.grid_columnconfigure(col, weight=1, uniform="col")

        lbl_day = ctk.CTkLabel(inputs_card, text="DAY", font=ctk.CTkFont(size=11, weight="bold"), text_color="#CBD5E1")
        lbl_day.grid(row=0, column=0, pady=(12, 2))
        self.entry_day = ctk.CTkEntry(inputs_card, placeholder_text="DD", justify="center", font=ctk.CTkFont(size=14, weight="bold"))
        self.entry_day.grid(row=1, column=0, padx=10, pady=(0, 15), sticky="ew")

        lbl_month = ctk.CTkLabel(inputs_card, text="MONTH", font=ctk.CTkFont(size=11, weight="bold"), text_color="#CBD5E1")
        lbl_month.grid(row=0, column=1, pady=(12, 2))
        self.entry_month = ctk.CTkEntry(inputs_card, placeholder_text="MM", justify="center", font=ctk.CTkFont(size=14, weight="bold"))
        self.entry_month.grid(row=1, column=1, padx=10, pady=(0, 15), sticky="ew")

        lbl_year = ctk.CTkLabel(inputs_card, text="YEAR", font=ctk.CTkFont(size=11, weight="bold"), text_color="#CBD5E1")
        lbl_year.grid(row=0, column=2, pady=(12, 2))
        self.entry_year = ctk.CTkEntry(inputs_card, placeholder_text="YYYY", justify="center", font=ctk.CTkFont(size=14, weight="bold"))
        self.entry_year.grid(row=1, column=2, padx=10, pady=(0, 15), sticky="ew")

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.pack(fill="x", padx=20, pady=12)

        calc_btn = ctk.CTkButton(
            btn_row,
            text="Calculate Age",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#0284C7",
            hover_color="#0369A1",
            corner_radius=10,
            height=40,
            command=self._calculate_age,
        )
        calc_btn.pack(side="left", expand=True, fill="x", padx=(0, 8))

        clear_btn = ctk.CTkButton(
            btn_row,
            text="Reset",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#334155",
            hover_color="#475569",
            corner_radius=10,
            height=40,
            command=self._reset_fields,
        )
        clear_btn.pack(side="right", expand=True, fill="x", padx=(8, 0))

        self.results_card = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=14)
        self.results_card.pack(fill="both", expand=True, padx=20, pady=(5, 20))

        self.status_lbl = ctk.CTkLabel(
            self.results_card,
            text="Enter your birth date above and click Calculate",
            font=ctk.CTkFont(size=12),
            text_color="#94A3B8",
        )
        self.status_lbl.pack(pady=(16, 8))

        stats_container = ctk.CTkFrame(self.results_card, fg_color="transparent")
        stats_container.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        for i in range(3):
            stats_container.grid_columnconfigure(i, weight=1, uniform="stat")

        self.box_years = self._make_stat_box(stats_container, 0, "YEARS", "-")
        self.box_months = self._make_stat_box(stats_container, 1, "MONTHS", "-")
        self.box_days = self._make_stat_box(stats_container, 2, "DAYS", "-")

        self.extra_info_lbl = ctk.CTkLabel(
            self.results_card,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#38BDF8",
        )
        self.extra_info_lbl.pack(pady=(0, 12))

    def _make_stat_box(self, parent, col, title, initial_val):
        box = ctk.CTkFrame(parent, fg_color="#0F172A", corner_radius=10)
        box.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        val_lbl = ctk.CTkLabel(
            box,
            text=initial_val,
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#F8FAFC",
        )
        val_lbl.pack(pady=(12, 0))

        title_lbl = ctk.CTkLabel(
            box,
            text=title,
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#64748B",
        )
        title_lbl.pack(pady=(0, 12))
        return val_lbl

    def _calculate_age(self):
        try:
            d = int(self.entry_day.get().strip())
            m = int(self.entry_month.get().strip())
            y = int(self.entry_year.get().strip())
            birth_dt = date(y, m, d)
        except ValueError:
            self.status_lbl.configure(text="Please enter a valid Gregorian calendar date.", text_color="#F87171")
            return

        today = date.today()
        if birth_dt > today:
            self.status_lbl.configure(text="Birth date cannot be in the future.", text_color="#F87171")
            return

        years = today.year - birth_dt.year
        months = today.month - birth_dt.month
        days = today.day - birth_dt.day

        if days < 0:
            months -= 1
            prev_month = 12 if today.month == 1 else today.month - 1
            prev_year = today.year - 1 if today.month == 1 else today.year
            month_days = [31, 29 if (prev_year % 4 == 0 and (prev_year % 100 != 0 or prev_year % 400 == 0)) else 28,
                          31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days += month_days[prev_month - 1]

        if months < 0:
            years -= 1
            months += 12

        self.box_years.configure(text=str(years))
        self.box_months.configure(text=str(months))
        self.box_days.configure(text=str(days))

        total_days = (today - birth_dt).days
        total_hours = total_days * 24
        self.status_lbl.configure(text="Age calculation successful", text_color="#34D399")
        self.extra_info_lbl.configure(
            text=f"Total Lived: {total_days:,} days  |  Approx: {total_hours:,} hours"
        )

    def _reset_fields(self):
        self.entry_day.delete(0, "end")
        self.entry_month.delete(0, "end")
        self.entry_year.delete(0, "end")
        self.box_years.configure(text="-")
        self.box_months.configure(text="-")
        self.box_days.configure(text="-")
        self.status_lbl.configure(text="Enter your birth date above and click Calculate", text_color="#94A3B8")
        self.extra_info_lbl.configure(text="")


if __name__ == "__main__":
    app = MasaAgeCalculator()
    app.mainloop()
