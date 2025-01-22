
from semantic_kernel.functions import kernel_function
import datetime

class TimePlugin:

    @kernel_function(
        name="time",
        description="Gets the current time"
    )
    def get_time(self):
        print("Getting the current time...")
        return datetime.datetime.now().strftime("%H:%M:%S")

    @kernel_function(
        name="date",
        description="Gets the current date"
    )
    def get_time(self):
        print("Getting the current date...")
        return datetime.datetime.now()