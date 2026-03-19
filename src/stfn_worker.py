import logging
import re

from PySide6.QtCore import QObject, Signal


class ProgressLogHandler(logging.Handler):
    def __init__(self, signal, max_epochs):
        super().__init__()
        self.signal = signal
        self.max_epochs = max_epochs
        self.epoch_pattern = re.compile(r"Epoch: (\d+)")

    def emit(self, record):
        msg = self.format(record)
        match = self.epoch_pattern.search(msg)
        if match:
            epoch_number = int(match.group(1))
            # print(f"DEBUG: epoch {epoch_number} out of {self.max_epochs}")
            self.signal.emit(epoch_number, self.max_epochs)


class STFNWorker(QObject):
    stfn_finished = Signal(object, dict)
    stfn_error = Signal(str)
    stfn_progress = Signal(int, int)

    def __init__(self, stfn, data_matrix, expert_rank, extra_data, max_epochs):
        super().__init__()
        self.stfn = stfn
        self.data_matrix = data_matrix
        self.expert_rank = expert_rank
        self.extra_data = extra_data
        self.max_epochs = max_epochs

    def run(self):
        mealpy_logger = logging.getLogger("mealpy")
        handler = ProgressLogHandler(self.stfn_progress, self.max_epochs)
        mealpy_logger.addHandler(handler)
        mealpy_logger.setLevel(logging.INFO)
        try:
            self.stfn.fit(self.data_matrix, self.expert_rank, log_to="console")
            self.stfn_finished.emit(self.stfn, self.extra_data)
        except Exception as e:
            self.stfn_error.emit(str(e))
        finally:
            mealpy_logger.removeHandler(handler)